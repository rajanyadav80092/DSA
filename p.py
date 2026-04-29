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
        self.head.next=node
        node.prev=self.head
    
    def remove_node(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
    
    def get_key(self,key):
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.add_to_front(node)
        return node.value
    
    def put(self,key,data):
        if key in self.cache:
            node=self.cache[key]
            self.remove_node(node)
            node.data=data
            self.add_to_front(node)
            return 
        node=Node(key,data)
        self.cache[key]=node
        self.add_to_front(node)
        if self.capacity<len(self.cache):
            last=self.tail.prev
            self.remove_node(last)
            del self.cache[last.key]
    
    def display(self):
        curr=self.head.next
        while curr!=self.tail:
            print(f"{curr.key}:{curr.data}",end=" ")
            curr=curr.next
        print("END")
lru=LRU(3)
lru.put(1,11)
lru.put(2,22)
lru.put(3,33)
lru.display()