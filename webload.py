from __future__ import division
from collections import Counter
import time

#required tornado version 3.0.1
#pip install tornado==3.0.1
import tornado
import tornado.ioloop
from tornado.ioloop import PeriodicCallback
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest

def loadweb(url,method='GET',totaltime=10,rate=1.0):
    '''url - url to request
    totaltime - total time test will take (seconds)
    rate - rate to send requests at (requests/second)
    returns a dictionary with key=http status code, value=# of responses
    '''

    http_client = AsyncHTTPClient(force_instance=True,max_clients = 10000)
    
    nrequests = int(totaltime * rate)
    waitrequest = 1/rate
    status = {'timestart':None,'requestcnt':0,'responsecnt':0,'responsestatus':Counter()}
    
    def _sendrequest():
        reqIx = status['requestcnt']
        status['requestcnt'] = reqIx+1
        if reqIx == 0:
            status['timestart'] = time.time()

        def _handleresponse(response):
            status['responsecnt'] += 1
            status['responsestatus'][response.code] += 1
            if status['responsecnt'] >= nrequests:
                print 'got all responses!'
                tornado.ioloop.IOLoop.instance().stop()
        
        http_request = HTTPRequest(url,
                            method,
                            body=None,
                            connect_timeout=2,
                            request_timeout=4)
 
        http_client.fetch(http_request, _handleresponse)
        
        if status['requestcnt'] >= nrequests:
            pc.stop()
            print 'sent all requests! actual rate: %.3f' %(status['requestcnt'] / (time.time()-status['timestart']))
    
    pc = PeriodicCallback(_sendrequest,waitrequest*1000)
    pc.start()
    
    tornado.ioloop.IOLoop.instance().start()
    return status['responsestatus']

if __name__ == '__main__':
    print loadweb('http://localhost:8080',totaltime=5.0,rate=1500)