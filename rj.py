class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
        self.prev=None
class Circulardoublylink:
    def __init__(self):
        self.head=None
    
    def insert_at_beggining(self,data):
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
        self.head=new_node
    
    def insert_at_between(self,data,key):
        new_node=Node(data)
        if self.head is None:
            print("list is empty key is not defined")
            return
        temp=self.head
        while temp.next != self.head:
            if temp.data==key:
                next_node=temp.next
                temp.next=new_node
                new_node.next=next_node
                next_node.prev=new_node
                new_node.prev=temp
                return
            temp=temp.next
        if temp.data==key:
            temp.next=new_node
            new_node.prev=temp
            new_node.next=self.head
            self.head.prev=new_node
            return
        print("key is not found please insert right key")
        return
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
        new_node.prev=temp
        self.head.prev=new_node
        return   
    def middle_value(self):
        if self.head is None:
            print("list is empty")
            return 
        slow=self.head
        fast=self.head
        while fast.next != self.head and fast.next.next != self.head:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)
        return
    
    def index_num(self):
        if self.head is None:
            print("list is empty not index")
            return 
        temp=self.head
        len=0
        while temp.next != self.head:
            len+=1
            temp=temp.next
        print(len)
        return 
    def length(self):
        if self.head is None:
            print("list is empty")
            return 
        temp=self.head
        len=1
        while temp.next != self.head:
            temp=temp.next
            len+=1
        print("length",len)
        return
    
    def print_forword(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while True:
            print(temp.data,end=" ")
            temp=temp.next
            if temp==self.head:
                break
    def print_backword(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        temp=self.head.prev
        while True:
            print(temp.data,end=" ")
            temp=temp.prev
            if temp==self.head.prev:
                break
    
    def delete_node(self,data):
        if self.head is None:
            print("list is empty") 
            return
        temp=self.head 
        if temp.data==data:
            if temp.next==self.head:
                self.head=None
                print(f"data is delete {data}") 
                return
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            temp=None
            print(f"data is removed {data}")
            return
        prev=None
        while temp.next != self.head and temp.data !=  data:
            prev=temp
            temp=temp.next
        if temp.data != data:
            print("data is not found")
            return
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        print(f"data is removed {data}")
        return
    
    def circular_list(self):
        if self.head is None:
            print("list is empty")
            return 
        slow=self.head  
        fast=self.head
        while True:
            fast=fast.next
            if fast.next is  None:
                print("not circular")
                return 
            slow=slow.next
            fast=fast.next
            if slow == fast:
                print("circular list")
                return
    def give_refrence(self,data):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp.next != self.head:
            if temp.data== data:
                print(temp)
                return 
            temp=temp.next
        if temp.data == data:
            print(temp)
            return
        print("data is not found please insert right data")
        return 
            
            

cll=Circulardoublylink()
cll.insert_at_beggining(1)
cll.insert_at_beggining(2)
cll.insert_at_beggining(3)
cll.insert_at_end(4)
cll.insert_at_between(5,4)
cll.print_forword()
print()
cll.circular_list()
cll.print_backword()
print()
cll.middle_value()
cll.index_num()
cll.length()
cll.give_refrence(5)

