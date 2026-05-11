class Graph:
    def __init__(self,vno):
        self.cortex_count=vno
        self.adj_matrix=[ [0]*vno for e in range(vno)]
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.cortex_count and 0<=v<self.cortex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("invalid cortex")
    
    def remove_edge(self,u,v,weight=0):
        if 0<=u<self.cortex_count and 0<=v<self.cortex_count:
            self.adj_matrix[u][v]=weight
        else:
            print("invalid cortex")
    
    def hash_edge(self,u,v):
        if 0<=u<self.cortex_count and 0<=u<self.cortex_count:
            if self.adj_matrix[u][v]!=0 or self.adj_matrix[v][u]!=0:
                return True
            else:
                return False
        else:
            print("invalid cortex")
    
    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))
g=Graph(5)
g.add_edge(0,1) 
g.add_edge(1,2)            
g.add_edge(2,3)            
g.add_edge(3,4)            
g.print_adj_matrix()                