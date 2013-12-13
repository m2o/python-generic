class Top(object):
	def __init__(self,id):
		self.__id = id
	
	def printA(self):
		print self.__id
	
class Bottom(Top):
	
	def __init__(self,id):
		self.__id = id
		super(Bottom,self).__init__(id+1)
		
	def printB(self):
		print self.__id
		
		
		
b = Bottom(100)

b.printA()
b.printB()