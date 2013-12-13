import httplib
import simplejson as json

URL = 'search.twitter.com'

def search(keyword,n=500):
    conn = httplib.HTTPConnection(URL)
    conn.request("GET", "/search.json?q=%s&rpp=%d" % (keyword,n))
    r1 = conn.getresponse()
    if r1.status!=200:
        raise Exception('status '+str(r1.status))
    data1 = r1.read()
    return json.loads(data1)['results']

if __name__ == '__main__':
    print search('kurac')[0]