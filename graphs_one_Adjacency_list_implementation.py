class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.num_vertices = 0

    def add_vertex(self, v1):
        self.num_vertices += 1
        


