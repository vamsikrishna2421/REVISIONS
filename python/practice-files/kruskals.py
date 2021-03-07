
class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, fromEdge, toEdge, weight):
        self.graph.append([fromEdge, toEdge, weight])

    
    def kruskals(self):
        coveredNodes=set()
        self.graph.sort(key=lambda item: item[2])
        MST=[]
        len=0
        for i in self.graph:
            if i[0] not in coveredNodes or i[1] not in coveredNodes:
                coveredNodes.add(i[0])
                coveredNodes.add(i[1])
                MST.append(i)
                len+=i[2]
        print(MST)

if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    g.kruskals()
    
    
    
    #OUTPUT:
    #[[2, 3, 4], [0, 3, 5], [0, 1, 10]]
