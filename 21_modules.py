import sys

print sys.modules.keys()

print list(sys.__dict__.keys())
print dir(sys)
print sys.__name__

print sys.path