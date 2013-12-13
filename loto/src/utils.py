import operator
import time

prod = lambda vals: reduce(operator.mul,vals,1)

def timeit(func):
    def timed(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()
        msg = '%s@%s - %2.2f sec' % (func.__module__,func.__name__,te-ts)
        print msg
        return result
    timed.__name__ = func.__name__
    timed.__doc__ = func.__doc__
    timed.__dict__.update(func.__dict__)
    return timed
