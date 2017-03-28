class my_Vertex:
	
		def __init__(self,key,posx,posy):
			self.id =key
			self.posx=posx
			self.posy=posy
			self.connectedTo={}

		def addNeighbor(self,nbr,weight=0):
			self.connectedTo[nbr] = weight

		def __str__(self):
			return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

		def getConnections(self):
			return self.connectedTo.keys()

		def getId(self):
			return self.id

		def getWeight(self,nbr):
			return self.connectedTo[nbr]

		def getPosX(self):
			return self.posx

		def getPosY(self):
			return self.posy
		
print "No errors in vertex"