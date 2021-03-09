class graph():
    def __init__(self,n):
        self.vertex={}
        self.n=n
    
    def add_edge(self,from_v,to_v):
        if from_v not in self.vertex.keys(): 
            self.vertex[from_v]=[to_v]
        else:
            self.vertex[from_v].append(to_v)
            
    def detect_cycle(self):
        #0-white, 1-gray, 2-black
        visited=[False]*(self.n)
        stack=[False]*(self.n)
        for i in self.vertex.keys():
            if visited[i]==False:
                if self.check_cycle_rec(visited,stack,i)==True:
                    return True
        return False
        
            
    def check_cycle_rec(self,visited,stack,current):
        visited[current]=True
        stack[current]=True
        if current in self.vertex.keys():
            for k in self.vertex[current]:
                if stack[k]==True:
                    return True
                elif visited[k]==False:
                    if self.check_cycle_rec(visited,stack,k)==True:
                        return True
        stack[current]=False
        return False

if __name__=='__main__':
    g=graph(6)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(3,0)
    g.add_edge(3,4)
    g.add_edge(4,5)
    g.add_edge(5,3)
    print(g.detect_cycle())
