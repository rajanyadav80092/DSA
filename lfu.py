class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.freq=1
        self.next=None
        self.prev=None
        
class Doublylinkedlist:
    def __init__(self):
        self.head=Node(0,0)
        self.tail=Node(0,0)
        
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def add_node(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
        
    def remove_node(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        
    def remove_last(self):
        if self.tail.prev == self.head:
            return None
        last=self.tail.prev
        self.remove_node(last)
        return last
    
    def is_empty(self):
        return self.head.next==self.tail
    
class LFU:
    def __init__(self,capacity):
        self.capacity=capacity
        self.key_table={}
        self.freq_table={}
        self.min_freq=0
        
    def get(self,key):
        if key not in self.key_table :
            return -1
        node=self.key_table[key]
        self._update_freq(node)
        return node.value
    
    def put(self,key,value):
        if self.capacity==0:
            return 
        if key in self.key_table:
            node=self.key_table[key]
            node.value=value
            self._update_freq(node)
        else:
            if len(self.key_table)>=self.capacity:
                min_list=self.freq_table[self.min_freq]
                node_to_remove=min_list.remove_last()
                del self.key_table[node_to_remove.key]
            new_node=Node(key,value)
            self.key_table[key]=new_node
            self.min_freq=1
            
            if 1 not in self.freq_table:
                self.freq_table[1]=Doublylinkedlist()
            self.freq_table[1].add_node(new_node)
    def _update_freq(self,node):
        freq=node.freq
        self.freq_table[freq].remove_node(node)
        
            
        self.freq_table[freq].remove_node(node)
        if self.freq_table[freq].is_empty():
            del self.freq_table[freq]
            if freq == self.min_freq:
                self.min_freq += 1
                
        node.freq+=1
        new_freq = node.freq
            
        if new_freq not in self.freq_table:
            self.freq_table[new_freq]=Doublylinkedlist()
        self.freq_table[new_freq].add_node(node)
    def display(self):
        print("\n---- LFU STATE ----")
        for freq in sorted(self.freq_table.keys()):
            print(f"Freq {freq} :", end=" ")

            dll = self.freq_table[freq]
            curr = dll.head.next

            while curr != dll.tail:
                print(f"[K:{curr.key}, V:{curr.value}]", end=" ")
                curr = curr.next

            print()
            print("-------------------\n")
lfu=LFU(2)
lfu.put(4,40)
lfu.put(1,11)
lfu.put(2,22)  
lfu.put(1,11)
lfu.put(3,30)
lfu.put(3,30)
lfu.put(3,30)
lfu.put(3,30)
lfu.put(9,99)
lfu.get(1)
lfu.display()