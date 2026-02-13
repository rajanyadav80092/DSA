class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class doublylinkedlist:
    def __init__(self):
        self.head=None
        
    def _insert_at_begging(self,data):
        new_node=Node(data)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node
        
        self.head=new_node 
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def print_backword(self):
        temp=self.head
        
        if self.head is None:
            return "empty doubly linked list"
        
        while temp.next:
            temp=temp.next
        
        while temp:
            print(temp.data,end=" ")
            temp=temp.prev
        print("None")
    
    def print_forword(self):
        temp=self.head
        
        if self.head is None:
            return "EMPTY DOUBLY LINKED LIST"
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("None")
    def count(self):
        len=0
        temp=self.head
        while temp:
            len+=1
            temp=temp.next
        return len
    def delete_node(self,key):
        temp=self.head
        
        if temp is not None and temp.data==key:
            self.head=temp.next
            if self.head is not None:
                self.head.prev = None
            return
    #     if temp is not None and temp.data == key:
    # self.head = temp.next
    # if self.head is not None:
    #     self.head.prev = None
    # return
    
        curr=None
        while temp is not None and temp.data != key :
            curr=temp
            temp=temp.next
        if temp is None:
            return "data is not found"
        curr.next=temp.next
        temp.prev=curr
        temp=None
    def insert_at_between(self,data,key):
        temp=self.head
        new_node=Node(key)
        while temp:
            if temp.next is None:
                temp.next=new_node
                return 
            if temp.data==data:
                next_node=temp.next
                temp.next=new_node
                new_node.prev=temp
                next_node.prev=new_node
                new_node.next=next_node
                return 
            temp=temp.next
            
                
    def midian(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    def flyod(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return "circular list"
        return "not circular list"
 
dll=doublylinkedlist()
dll.insert_at_end(300)
dll._insert_at_begging(40)
dll._insert_at_begging(30)
dll._insert_at_begging(32)
dll._insert_at_begging(31)
dll.insert_at_between(300,56)
# dll.print_backword() 
dll.print_forword() 
print(dll.midian()) 
print(dll.flyod())
print(dll.count())   