import urllib2
import StringIO
import gzip
import shelve
from collections import OrderedDict

from parse import parse_html
from data import dbutils
from settings import DATA_URL
from utils import timeit

@timeit
def fetch_remote_item_data():
    return parse_html(fetch_html())

def fetch_local_item_data():
    db = dbutils.open()
    try:
        local_data = db['data']
    except KeyError:
        return {}
    finally:
        dbutils.close()
    return local_data

def save_item_data(remote_data):
    db = dbutils.open()
    local_data = db.get('data',None)
    if local_data is None:
        local_data = {}

    local_dates = local_data.keys()
    new_instances = filter(lambda ri: ri['date'] not in local_dates,remote_data)
    print 'saved %d instances' % len(new_instances)
    [local_data.__setitem__(ni['date'],ni) for ni in new_instances]
    db['data'] = OrderedDict((instance['date'],instance) for instance in
                             sorted(local_data.values(),key=lambda d: d['date']))
    dbutils.close()

@timeit
def fetch_html():
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding':'gzip,deflate,sdch',
               'Accept-Language':'en-US,en;q=0.8',
               'Host':'www.supersport.hr',
               'Referer':'http://www.supersport.hr/rezultati/loto',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1'}

    request = urllib2.Request(DATA_URL,headers=headers)
    f = urllib2.urlopen(request)
    #print f.info()
    gzipped_html = f.read()
    f.close()
    return ungzip(gzipped_html)

def ungzip(gzipped_data):
    data = StringIO.StringIO(gzipped_data)
    gzipper = gzip.GzipFile(fileobj=data)
    return gzipper.read()

if __name__ == '__main__':
    #print fetch_html()
    data = fetch_remote_item_data()
    save_item_data(data)
    #fetch_local_item_data()

    #print fetch_local_item_data()