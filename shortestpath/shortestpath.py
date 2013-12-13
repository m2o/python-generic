import sys
import math
import heapq
from collections import deque
from operator import itemgetter

class Problem(object):

	def initialize(self,map,size):
		self.size = size
		
		self.map = map
		self.sindex = filter(lambda (k,v): v.lower()=='s',map.items())[0][0]
		self.eindex = filter(lambda (k,v): v.lower()=='e',map.items())[0][0]
		
		self.currentindex = self.sindex
		self.currentlen = 0
		
	def copy(self):
		np = Problem()
		np.size = self.size
		np.map = dict(self.map)
		np.sindex = self.sindex
		np.eindex = self.eindex
		np.currentindex = self.currentindex
		np.currentlen = self.currentlen
		return np
		
	def iscomplete(self):
		return self.currentindex == self.eindex
	
	def printmap(self):
		
		for i in xrange(0,self.size):
			line = [self.map[(i,j)] for j in xrange(0,self.size)]
			print ''.join(line)
		
	def move(self,hor,plus):
	
		(ci,cj) = self.currentindex
		
		if hor and plus:
			(ni,nj) = (ci,cj+1)
		elif hor and not plus:
			(ni,nj) = (ci,cj-1)
		elif not hor and plus:
			(ni,nj) = (ci+1,cj)
		elif not hor and not plus:
			(ni,nj) = (ci-1,cj)
			
		if ni < 0 or ni >= self.size:
			return None
			
		if nj < 0 or nj >= self.size:
			return None
			
		nextindex = (ni,nj)
		nextvalue = self.map[nextindex]
		
		if nextvalue not in ('E','.'):
			return None
			
		np = self.copy()
		if np.map[nextindex] != 'E':
			np.map[nextindex] = 'o'
		np.currentlen += 1
		np.currentindex = nextindex
		return np
		
	def children(self):
		for hor in (True,False):
			for plus in (True,False):
				np = self.move(hor,plus)
				if np:
					yield np
	
def solvebfs(p):
	
	tasks = deque()
	tasks.append(p)
	
	cnt = 0
	
	while tasks:
		
		#print '#%d' % (cnt,)
		cnt+=1
		
		p = tasks.popleft()
		
		if p.iscomplete():
			yield (p.currentlen,p)
			continue
		
		tasks.extend(p.children())  #BFS
		
		#for c in p.children(): #DFS
			#tasks.appendleft(c)
			

def solveastar(p,g,h):
	
	f = lambda p: g(p)+h(p)
	tasks = []
	heapq.heappush(tasks,(f(p),p))
	
	while tasks:
		(fp,p) = heapq.heappop(tasks)
		
		if p.iscomplete():
			yield (p.currentlen,p)
			continue
			
		for c in p.children():
			heapq.heappush(tasks,(f(c),c))

if __name__ == '__main__':
	size = int(sys.stdin.readline().strip())
	value = [sys.stdin.readline().strip() for i in xrange(0,size)]

	map = dict(((i,j),c) for (i,v) in enumerate(value) for (j,c) in enumerate(v))
	p = Problem()
	p.initialize(map,size)
	
	#for (l,s) in solvebfs(p):
		#print '\n',l
		#s.printmap()
		
	def h(p):
		(ci,cj) = p.currentindex
		(ei,ej) = p.eindex
		return math.fabs(cj-ej)+math.fabs(ci-ei)
		
	for (l,s) in solveastar(p,lambda p: p.currentlen, h):
		print '\n',l
		s.printmap()
		break
	
