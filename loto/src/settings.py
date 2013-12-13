import os

from analysis.deciders import sorted_last_seen_middle

SRC_HOME =  os.path.dirname(__file__)

DATA_URL = "http://www.supersport.hr/rezultati/loto"
DATA_NAME = "TAL. WIN FOR LIFE 10/20"
DATA_DB_FILE = os.path.join(SRC_HOME,'.db')

ANALYSIS_NUM_CHOOSER = sorted_last_seen_middle

K = 2.0
MT = 0.05
ITEMS = range(1,21)

if os.environ.get('LOTO_LOCAL',None):
    SMTP_SERVER = 'mail.t-com.hr'
else:
    SMTP_SERVER = 'localhost'

NOTIFY_FROM = 'notify@loto.com'
NOTIFY_TO = ['t.pivcevic@gmail.com',]
NOTIFY_LOG = 15