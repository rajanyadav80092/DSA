from collections import deque
class Graph:
    def __init__(self):
        self.adj_list={}
        self.visited=set()
        
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
    
    def print_traversal(self):
        n=len(self.adj_list)
        for i in range(n):
            print(f"neightbor {i} : {self.adj_list[i]}")
        return
    
    def _bfs(self):
        self.visited.clear()
        components = []
        
        
        
        n=len(self.adj_list)
        for i in range(n):
            if i not in self.visited:
                compo=self.bfs(i,self.visited)
                components.append(compo)
        count=0
        for i in range(len(components)):
            count+=1
        print("components :",components)
        return count
    
    def bfs(self,i,visited):
        queue=deque([i])
        visited.add(i)
        ans=[]
        
        while queue:
            a=queue.popleft()
            ans.append(a)
            for i in self.adj_list[a]:
                if i not in  visited:
                    visited.add(i)
                    queue.append(i)
                    
        return ans
    
    
    def dfs(self,node,visited,ans):
        visited.add(node)
        ans.append(node)
        
        for i in self.adj_list[node]:
            if i not in visited:
                self.dfs(i,visited,ans)
        return ans
        
    
   
    
                
g=Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)
# g.print_graph()
# print(g._bfs())
print(g.dfs(0,set(),[]))
# g.print_traversal()
        
            
            
        