class Node:
    def __init__ (self,data):
        self.prev=None
        self.data=data
        self.next=None
class Circulardoublylinked:
    def __init__(self):
        self.head=None
    #permirised constructor
    def insert_at_begining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            new_node.prev=self.head
            return
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        return
    
    def insert_at_between(self,data,key):
        new_node=Node(key)
        temp=self.head
        while temp.next != self.head:
            if temp.data ==data:
                next_node=temp.next
                temp.next=new_node
                new_node.prev=temp
                new_node.next=next_node
                next_node.prev=new_node
                return
            temp=temp.next   
        if temp.data==data:
            temp.next=new_node
            new_node.prev=temp
            self.head.prev=new_node
            new_node.next=self.head
            return
        return print("data not found please put correct number")
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
            return
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
        self.head.prev=new_node
        new_node.prev=temp
        return
        
    @property
    def index(self):
        len=0
        temp=self.head
        while temp.next != self.head:
            len+=1
            temp=temp.next
        return print("index",len)
    
    def circular_list(self):
        if self.head is None:
            return print("list is empty")
        slow=self.head
        fast=self.head
        while True:
            fast=fast.next
            if fast is None:
                return print("not circular")
            fast=fast.next
            slow=slow.next
            if slow==fast:
                return print("circular list")
    
    def midiam(self):
        if self.head is None:
            return print("list is empty")
        fast=self.head 
        slow=self.head
        while fast.next !=self.head and fast.next.next!=self.head:
            slow=slow.next 
            fast=fast.next.next
        return print(slow.data)
    
    
    @property
    def count(self):
        if self.head is None:
            return print("list is empty not length")
        lenth=1
        temp=self.head
        while temp.next!=self.head:
            lenth+=1
            temp=temp.next
        return print("count",lenth)   
        
    
    @property
    def print_forword(self):
        if self.head is None:
            return print("list is empty")
        temp=self.head
        while temp.next != self.head:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data,end=" ")
        return 
    #default constructor
    @property
    def print_backword(self):
        if self.head is None:
            return print("list is empty")
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        temp=self.head.prev
        while True:
            print(temp.data,end=" ")
            temp=temp.prev
            if temp==self.head.prev:
                break
    def delete_node(self,key):
        if self.head is None:
            return print("circular list is empty")
        temp=self.head
        if temp.data==key:
            if temp.next is self.head:
                self.head=None
                return f"{key} deleted"
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            temp=None
            return print(f"{key} is deleted successfully")
        prev=None
        while temp.next != self.head and temp.data !=key:
            prev=temp
            temp=temp.next
        if temp.data != key:
            return print("data is not found")
        
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        return print(f"{key} deleted successfully")
    
cll=Circulardoublylinked()

cll.insert_at_begining(10)
cll.insert_at_begining(101)
cll.insert_at_begining(102)
cll.insert_at_between(10,100)
cll.print_forword
print()
cll.insert_at_between(10,22)
cll.insert_at_end(111)
cll.index
cll.count
cll.print_forword
print()
cll.circular_list()
cll.midiam
cll.delete_node(102)  
cll.print_forword   
print()
cll.print_backword      
        