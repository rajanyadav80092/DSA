# class Node:
#     def __init__(self,key,value):
#         self.value=value
#         self.key=key
#         self.next=None
#         self.prev=None

# class LRU:
#     def __init__(self,capacity):
#         if capacity <=0:
#             raise ValueError("capacity must be positive")
#         self.capacity=capacity
#         self.cache={}
        
#         self.head=Node(0,0)
#         self.tail=Node(0,0)
        
#         self.head.next=self.tail
#         self.tail.prev=self.head
    
#     def add_front(self,node):
#         node.next=self.head.next
#         self.head.next.prev=node
#         self.head.next=node
#         node.prev=self.head
        
#     def remove(self,node):
#         prev=node.prev
#         nxt=node.next
#         prev.next=nxt
#         nxt.prev=prev
    
#     def get(self,key):
#         if key not in self.cache:
#             return -1
#         node=self.cache[key]
#         self.remove(node)
#         self.add_front(node)
#         return node.value
    
#     def put(self,key,value):
#         if key in self.cache:
#             node=self.cache[key]
#             node.value=value
#             self.remove(node)
#             self.add_front(node)
#             return
#         node=Node(key,value)
#         self.cache[key]=node
#         self.add_front(node)
#         if len(self.cache)>self.capacity:
#             last=self.tail.prev
#             self.remove(last)
#             del self.cache[last.key]
            
#     def display(self):
#         if not self.cache:
#             return "lru is empty"
#         temp=self.head.next
#         while temp !=self.tail:
#             print(f"{temp.key} : {temp.value}",end=" ")
#             temp=temp.next
#         print("END")
# lru=LRU(0)
# lru.put(1,11)
# lru.put(2,22)
# lru.put(1,1)
# lru.put(3,13)
# lru.display()


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Linked:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        return
    
    def partition(self,x):
        if self.head is None:
            return "list is empty"
        
        small_dummy=Node(0)
        large_dummy=Node(0)
        
        small=small_dummy
        large=large_dummy
        
        temp=self.head
        while temp:
            if temp.data<x:
                small.next=temp
                small=small.next
            else:
                large.next=temp
                large=large.next
            temp=temp.next
        large.next=None
        small.next=large_dummy.next
        return small_dummy.next
    # def partition(self, x):
    #     arr=[]
    #     temp=self.head
    #     while temp:
    #         arr.append(temp.data)
    #         temp=temp.next
        
    #     arr1=[]
    #     arr2=[]
    #     for i in range(len(arr)):
    #         if arr[i]<x:
    #             arr1.append(arr[i])
    #         else:
    #             arr2.append(arr[i])
                
    #     dummy=Node(0)
    #     temp=dummy
    #     for i in arr1:
    #         temp.next=Node(i)
    #         temp=temp.next
    #     for j in arr2:
    #         temp.next=Node(j)
    #         temp=temp.next
    #     self.head=dummy.next
    #     return self.head
    
    def print(self):
        temp=self.head
        while temp:
            print(f"{temp.data} " ,end=" ")
            temp=temp.next
sll=Linked()
sll.insert(2)
sll.insert(5)
sll.insert(2)
sll.insert(3)
sll.insert(4)
sll.insert(1)
sll.partition(3)
sll.print()

