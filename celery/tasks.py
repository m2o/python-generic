import time
from datetime import datetime

from celery.task import task,Task
from celery.exceptions import SoftTimeLimitExceeded

@task(max_retries=2,default_retry_delay=20,time_limit=10,soft_time_limit=7,track_started=True)
def add(a,b):
    task_data = {'name':add.name,\
                 'max_retries':add.max_retries,\
                 'default_retry_delay':add.default_retry_delay,\
                 'rate_limit':add.rate_limit,
                 'time_limit':add.time_limit,
                 'soft_time_limit':add.soft_time_limit}
    
    req_data = {'id':add.request.id,\
    'pargs':add.request.args,\
    'kwargs':add.request.kwargs,\
    'retries':add.request.retries}
    
    logger = add.get_logger()
    logger.info('task data:%s'%str(task_data))
    logger.info('request data:%s'%str(req_data))
    
    #try:
    #    time.sleep(15)
    #except SoftTimeLimitExceeded,e:
    #    return "Had to end in a hurry, sorry!"
    
    #try:
    #    5/0
    #except Exception,e:
    #    add.retry(countdown=10,exc=e)
    
    add.update_state(state='SLEEP',meta={'amount':5})
    time.sleep(5)
    
    return a*2+b*2
    
class BaseTask(Task):
    abstract = True
    
    def execute(self,*args,**kwargs):
        print 'task executing - get_logger() y u no work here?'
        super(BaseTask,self).execute(*args,**kwargs)

    def after_return(self,status,retval,*args,**kwargs):
        self.get_logger().info('task returned status %s return value "%s"'%(status,retval))
        
    def on_failure(self,exc,*args,**kwargs):
        self.get_logger().info('task failed exception "%s"'%(exc,))

class PeriodicTask(BaseTask):
    
    ignore_result = True
    
    def run(self):
        pass
        #do something smart here
        
class DateFormatterTask(BaseTask):
    
    def run(self,date,format):
        return date.strftime(format)
        
class DateTimeTask(BaseTask):
    
    time_limit=10
    soft_time_limit=7
    track_started=True
    
    def run(self):
        logger = self.get_logger()
        
        task_data = {'name':self.name,\
                     'max_retries':self.max_retries,\
                     'default_retry_delay':self.default_retry_delay,\
                     'rate_limit':self.rate_limit,
                     'time_limit':self.time_limit,
                     'soft_time_limit':self.soft_time_limit}
    
        req_data = {'id':self.request.id,\
                    'pargs':self.request.args,\
                    'kwargs':self.request.kwargs,\
                    'retries':self.request.retries}
                    
        logger.info('task data:%s'%str(task_data))
        logger.info('request data:%s'%str(req_data))
        
        return str(datetime.now())
