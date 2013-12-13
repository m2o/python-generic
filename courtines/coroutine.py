#decorator
from functools import wraps

def coroutine(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        a = func(*args,**kwargs)
	a.next() #priming
	return a
    return wrapper


