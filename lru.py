class Node:
    def __init__(self,key,data):
        self.key=key
        self.data=data
        self.next=None
        self.prev=None

class LRU:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}
        
        self.head=Node(0,0)
        self.tail=Node(0,0)
        
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def add_front(self,node):
        node.next=self.head.next
        self.head.next.prev=node
        node.prev=self.head
        self.head.next=node
    
    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
    
    def get_key(self,key):
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.add_front(node)
        return node.data
    
    def put(self,key,data):
        if key in self.cache:
            node=self.cache[key]
            node.data=data
            self.remove(node)
            self.add_front(node)
            return
        node=Node(key,data)
        self.cache[key]=node
        self.add_front(node)
        if len(self.cache)>self.capacity:
            last=self.tail.prev
            self.remove(last)
            del self.cache[last.key]
    
    def display(self):
        if not self.cache :
            return -1
        temp=self.head.next
        while temp!= self.tail:
            print(f"{temp.key}: {temp.data}",end=" ")
            temp=temp.next
        print("END")
lru=LRU(3)
lru.put(1,11)
lru.put(2,22)
lru.put(1,111)
lru.put(3,33)
lru.put(4,44)
x=lru.get_key(1)
print(x)
lru.display()