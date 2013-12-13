from datetime import datetime,timedelta

from prov_core.tasks import AddTask

##import tasks
##
##
##execution_time = datetime.now() + timedelta(seconds=15)
##kwargs = {}
##kwargs['eta'] = execution_time
###kwargs['countdown'] = 2
##result = tasks.DateTimeTask.apply_async(**kwargs)
##print result.get()
##
##result = tasks.DateFormatterTask.delay(date=datetime.now(),format='%Y %b %d')
##print result.get()


print AddTask.delay(4,3).get()