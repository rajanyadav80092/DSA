class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
    
    def union(self,u,v):
        px=self.find(u)
        py=self.find(v)
        
        if px==py:
            return 
        if self.size[px]<self.size[py]:
            px,py=py,px
        self.parent[py]=px
        self.size[px]+=self.size[py]
    
    def find(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    
    def group(self,n):
        g=0
        for i in range(1,n+1):
            if self.find(i)==i:
                g+=1
        return g
    
    def print_all(self,n):
        for i in range(n+1):
            dsu.find(i)
        print(self.size)
            
        return self.parent

dsu=DSU(5)
dsu.union(1,2)
dsu.union(3,4)
dsu.union(4,5)
dsu.union(2,3)
print(dsu.print_all(5))
print(dsu.group(5))