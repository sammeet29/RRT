'''
Sammeet Koli
skoli@uncc.edu
Uncc
Implementation of DFS algorithm on graph datastructure 
Using graph datastrucute my_Graph
'''
from Graph import my_Graph
from Vertex import my_Vertex

class Dfs:
	
	
	def __init__(self,graph,start_vertex,end_vertex):
		self.g = graph
		#v = vertex
		#self.sv = self.g.getVertex(start_vertex)
		self.ev = end_vertex
		self.stack = []
		self.visited = {}
		self.path_found = False
		#self.stack.append(self.sv)
		self.stack.append(start_vertex)
		for v in self.g.vertList:
			self.visited[v]=False
		#print "Start dfs"
		self.visited[start_vertex.getId()]=True
		for child_v in start_vertex.getConnections():
			if child_v == end_vertex or self.path_found:
				#print "stop in init"
				break
			if self.visited[child_v.getId()] == False:
				self.stack.append(child_v)
				#print "append child",child_v.getId()
				#self.visited[child_v]=True
				self.dfs_visit(child_v)
			#self.stack.pop()
				
	def printPath(self):
		'''
		#print "len: ",len(self.stack)
		for i in range(len(self.stack)):
			#print self.stack.pop().getId()
		'''
		return self.stack
				
	def dfs_visit(self,u):
		self.visited[u.getId()]=True
		#print "dfs visit",u.getId()
		if self.path_found:
			return
		
		for w in u.getConnections():
			#self.stack.append(w)
			#w_ver = self.g.getVertex(w)
			if w == self.ev:
				#print "stop in dfs_visit",w.getId()
				self.stack.append(w)
				self.path_found = True
				break
			elif self.visited[w.getId()]:
				#print "continue : ",w.getId()
				continue
			elif self.path_found:
				return
			else:
				#self.visited[w.getId()]= True
				self.stack.append(w)
				#print "append ",w.getId()
				self.dfs_visit(w)
		if self.path_found==False:
			v=self.stack.pop()
			#print "pop:",v.getId()
			
###print "no errors in dfs"		
