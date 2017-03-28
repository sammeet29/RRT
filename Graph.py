'''
Sammeet Koli
skoli@uncc.edu
Uncc
Graph class for implementing a undirected graph
'''

from Vertex import my_Vertex
import math

class my_Graph:
	'''
	Name : init
	Inputs: None
	Outputs: None
	Function: Initializes the object of my_Graph class
	'''	
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0
	'''
	Name : add vertex
	Inputs: x-position, y-position 
	Outputs: Vertex object
	Function: adds a new vertex to the graph
	'''	
	def addVertex(self,key,posx,posy):
		self.numVertices = self.numVertices + 1
		newVertex = my_Vertex(key,posx,posy)
		self.vertList[key] = newVertex
		return newVertex
	
	'''
	Name : getVertex 
	Inputs: id of the vertex
	Outputs: my_Vertex object
	Function: returns a vertex object from id of the vertex
	'''	
	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None
		
	def __contains__(self,n):
		return n in self.vertList

	def addEdge(self,f,t):
		fv = self.getVertex(f)
		tv = self.getVertex(t)
		fx = fv.getPosX()
		fy = fv.getPosY()
		tx = tv.getPosX()
		ty = tv.getPosY()
		weight = self.cost_func(fx,fy,tx,ty)
		self.vertList[f].addNeighbor(self.vertList[t], weight)
		self.vertList[t].addNeighbor(self.vertList[f],weight)
		
	def cost_func(self,fx,fy,tx,ty):
		#print("%d,%d,%d,%d"%(fx,tx,fy,ty))
		cost = math.sqrt( (tx - fx)**2 + (ty - fy)**2 ) 
		return cost
	

	def getNearestNode(self,xin,yin):
		min_dist = 999;
		for v in self.vertList:
			vertex = self.getVertex(v)
			dist = self.cost_func(vertex.getPosX(),vertex.getPosY(),xin,yin)
			#print vertex.getId(),dist
			if dist<min_dist :
				min_dist = dist
				nearestVertex = vertex
		#print "nearest node: %d,%d"%(nearestVertex.getPosX(),nearestVertex.getPosY())
		#print nearestVertex.getId()
		return nearestVertex;
		
	
print "no errors in graph"
