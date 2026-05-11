class Graph:
    def __init__(self):
        self.adj_list={}
    
    def add_vertex(self,v):
        if v not in self.adj_list:
            self.adj_list[v]=[]
    
    def add_edge(self,u,v,bidirectional=True):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)
        if bidirectional: #directional means one ways graph 1---->2 bidirectional means two ways graph 1<----->2
            self.adj_list[v].append(u)
    
    def print_graph(self):
        for node in self.adj_list:
            print(f"{node}-> {self.adj_list[node]}")
g=Graph()
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.print_graph()
        
            
            
        