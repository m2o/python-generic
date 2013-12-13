import time
import pprint
from textwrap import dedent
import shelve
from datetime import datetime
import os

from data.fetch import fetch_remote_item_data
from data.fetch import save_item_data
from data import dbutils
from analysis.statistics import extract_stats
from sendmail import send
from settings import NOTIFY_FROM
from settings import NOTIFY_TO
from settings import NOTIFY_LOG
from settings import ANALYSIS_NUM_CHOOSER

current_decider = ANALYSIS_NUM_CHOOSER

format_log = lambda d: '%(date)s - %(nums)s - %(prediction_prev)d - %(outcome)s' % d

def _log(data,index):
    instance = data[index]
    prev_instance = data[index - 1]

    date = instance['date']
    nums = instance['nums']

    stats = extract_stats(data,index)
    stats_prev = extract_stats(data,index-1)
    prediction = current_decider(stats)
    prediction_prev = current_decider(stats_prev)

    outcome = 'SUCCESS' if prediction_prev in nums else 'FAIL'

    return {'date':date,
            'nums':nums,
            'prediction_prev':prediction_prev,
            'prediction':prediction,
            'predictor':current_decider.__name__,
            'outcome':outcome,
            'stats':stats}

def fetch_and_save_data():
    data = list(fetch_remote_item_data())
    save_item_data(data)
    return data

def run(force=False):

    data = list(fetch_and_save_data())
    db = dbutils.open()

    #back log
    end_index = len(data)-1
    begin_index = end_index - NOTIFY_LOG
    log_dicts = [_log(data,i) for i in range(begin_index,end_index+1)]

    #dates
    last_instance = log_dicts[-1]
    data_date = last_instance['date']
    current_date = datetime.now().replace(minute=0,second=0,microsecond=0)
    notified_date = db.get("notified_date",None)

    #check notify
    if not force and notified_date == data_date:
        print 'notification ignored - already sent notification for date %s' % (notified_date,)
    elif not force and current_date!=data_date:
        print 'notification ignored - data not yet available for date %s' % (current_date,)
    else:
        db["notified_date"] = data_date
        _notify(log_dicts, force)
    dbutils.close()

def _notify(log_dicts, force):
    last_instance = log_dicts[-1]
    data_date = last_instance['date']
    nums = last_instance['nums']
    prediction_prev = last_instance['prediction_prev']
    outcome = last_instance['outcome']
    prediction_next = last_instance['prediction']
    last_seen = '  '.join([str(v) for v in last_instance['stats']['last_seen']])
    percent_10 = '  '.join(['%.2f' % round(percent,2) for percent in last_instance['stats']['percents'][10]])

    back_log = '\n'.join([format_log(log_dict) for log_dict in reversed(log_dicts[:-1])])

    subject = 'notify %s %s - pred:%d' % (data_date,outcome,prediction_next)
    body = dedent('''\
            date: %(data_date)s
            nums: %(nums)s
            prediction(prev): %(prediction_prev)d - %(outcome)s
            prediction(next): %(prediction_next)d
            last seen: %(last_seen)s
            percent 10: %(percent_10)s

            log:
            %(back_log)s
            ''') % vars()

    print 'notification sent %s%s' % (data_date,' [FORCED]' if force else '')
    send(subject,NOTIFY_FROM,NOTIFY_TO,body)

if __name__ == '__main__':
    import sys
    run(force='--force' in sys.argv)