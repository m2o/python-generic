import re
import itertools
import random
import shelve
from pprint import pprint
from datetime import datetime
from datetime import timedelta

from BeautifulSoup import BeautifulSoup

from settings import K
from settings import MT
from settings import ITEMS
from settings import DATA_NAME
from utils import prod
from utils import timeit

def _extract_datestr_from_tr(tr):
    return tr.find('td',attrs='vrijemeRezultata').contents[0].strip()

def parse_html(html):
    soup = BeautifulSoup(html)
    tr_parent = soup.find(text=DATA_NAME).parent.parent
    tr_parent_next = tr_parent.findNextSibling('tr',attrs={'class':re.compile('parentPonuda')})
    tr_child_last = tr_parent_next.findPreviousSibling('tr')

    datestr_first = _extract_datestr_from_tr(tr_parent)
    datestr_last = _extract_datestr_from_tr(tr_child_last)

    now_year = int(datetime.now().strftime('%Y'))
    date_first = datetime.strptime(datestr_first,'%d.%m.')
    date_last = datetime.strptime(datestr_last,'%d.%m.')

    print 'parsing interval %s - %s' % (datestr_last,datestr_first)

    year_last = now_year
    if date_last > date_first:
        print 'detected new year!'
        raise NotImplementedError('detected new year!')
        year_last -=1
    current_year = year_last

    def gen_nums(tr_parent):
        def extract(tr):
            date_str = tr.find('td',attrs='vrijemeRezultata').contents[0]
            _id = int(tr.find('td',attrs='koloRezultata').contents[0])
            n = (_id-1) % 15
            date = datetime.strptime('%s%d. %d:00'% (date_str,current_year,n+8),'%d.%m.%Y. %H:%M')
            nums = [int(div.contents[0]) for div in tr.findAll('div',attrs='lotoRezultatBroj')]
            return {'date':date,'id':_id,'nums':nums,'n':n}

        current = tr_child_last
        _break = False

        while True:
            yield extract(current)
            if _break:
                break
            current = current.findPreviousSibling('tr',attrs={'class':re.compile('childPonuda|parentPonuda')})
            _class = dict(current.attrs).get('class')
            if _class == 'parentPonuda':
                _break=True

    return gen_nums(tr_parent)
