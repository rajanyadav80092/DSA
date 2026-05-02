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
        
    def add_to_front(self,node):
        node.next=self.head.next
        self.head.next.prev=node
        node.prev=self.head
        self.head.next=node
        
    def _remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
    
    def get(self,key):
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self._remove(node)
        self.add_to_front(node)
        return node.data
    
    def put(self,key,data):
        if self.capacity==0:
            print("capacity is 0")
            return
        if key in self.cache:
            node=self.cache[key]
            node.data=data
            self._remove(node)
            self.add_to_front(node)
            return
        node=Node(key,data)
        self.cache[key]=node
        self.add_to_front(node)
        if len(self.cache)>self.capacity :
            last=self.tail.prev
            self._remove(last)
            del self.cache[last.key]
    
    def display(self):
        if self.capacity==0:
            print("not store data in capacity")
            return
        curr=self.head.next
        while curr!=self.tail:
            print(f"{curr.key} : {curr.data}",end=" ")
            curr=curr.next
        print("END")
    
lru=LRU(3)
lru.put(1,11)
lru.put(2,22)
lru.put(3,33)
lru.put(1,111)
lru.put(4,44)
lru.display()
            
            
        