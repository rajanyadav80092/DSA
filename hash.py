class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
        
class Circulardoublylinked:
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            return
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        temp.next=self.head
        
    @property
    def print_forword(self):
        if self.head is None:
             print("circular limked list is empty ")
             return
        temp=self.head
        while temp.next!=self.head:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data,end=" ")
    @property
    def print_backword(self):
        if self.head is None:
            return "circular doubly linked list is empty"
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        while temp.prev:
            print(temp.data,end=" ")
            temp=temp.prev
        print(temp.data,end=" ")
        
    @property
    def count(self):
        length=1
        temp=self.head
        while temp.next!=self.head:
            length+=1
            temp=temp.next
        return length
    
    @property
    def index1(self):
        lent=0
        temp=self.head
        while temp.next!=self.head:
            lent+=1
            temp=temp.next
        return lent
    @property
    def floyd(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return "circular linked list"
        return "not circular linked list"
            
    def midiam(self):
        slow=self.head
        fast=self.head
        
        while fast.next!=self.head and fast.next.next != self.head:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    
    def delete_node(self,key):
        if self.head is None:
            print("list is empty ")
            return
        temp=self.head
        if temp.data == key:
            if temp.next == self.head:
                self.head=None
                return key
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            temp=None
            return key
        prev=None
        while temp.next != self.head and temp.data !=key:
            prev=temp
            temp=temp.next
        if temp.next == self.head:
            return "data is not found"
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        return key
        
                    
                    
        
cdl=Circulardoublylinked()
cdl.insert_at_beginning(10)
cdl.insert_at_beginning(12)
cdl.insert_at_beginning(13)
cdl.insert_at_beginning(14)
cdl.print_forword
print()
cdl.print_backword
print()
print("index",cdl.index1)
print("length",cdl.count)
print(cdl.floyd)
print(cdl.midiam())   
print(cdl.delete_node(10))  
cdl.print_forword 

        