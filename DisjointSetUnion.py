class Disjoint:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
    
    def union(self,nums,nums2):
        px=self.find(nums)
        py=self.find(nums2)
        
        if px==py:
            return
        if self.size[px]<self.size[py]:
            px,py=py,px
        self.parent[py]=self.find(self.parent[px])
        self.size[px]+=self.size[py]
    
    def find(self,x):
        if self.parent[x]==x:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def group(self):
        count=0
        for i in range(1,len(self.parent)):
            if self.find(i)==i:
                count+=1
        return count
        
    def printSize(self):
        print(self.parent)
        print(self.size)
d=Disjoint(5)
d.union(1,2)
d.union(3,4)
d.union(4,5)
d.union(1,5)
d.printSize()
print(d.group())
print(d.find(4))
d.printSize()
print(d.group())
