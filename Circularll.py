class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedlist:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            return
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
        
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
        temp.next=new_node
        self.head=new_node
        
    def insert_at_between(self,data,key):
        new_node=Node(key)
        temp=self.head
        while temp.next !=self.head:
            if temp.data==data:
                next_node=temp.next
                temp.next=new_node
                new_node.next=next_node
                return
            temp=temp.next
        if temp.data == data:
            temp.next=new_node
            new_node.next=self.head
            return
            
        return print("data is not found")        

    def count(self):
        length=0
        temp=self.head
        while True:
            length+=1
            temp=temp.next
            if temp==self.head:
                break
        return length
    
    def floyd(self):
        fast=self.head
        slow=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow == fast:
                return "circular"
        return "not circular"
    
    def print_list(self):
        if self.head == None:
            print("cll is empty")
            return
        temp=self.head
        while temp.next != self.head:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data ,end=" ")
            
        
        
        
cll=CircularLinkedlist()
cll.insert_at_end(10)
cll.insert_at_end(110)
cll.insert_at_end(101)
cll.insert_at_end(100)
cll.insert_at_end(11)
cll.insert_at_end(1011)
cll.insert_at_beginning(111)
cll.insert_at_beginning(222)
print(cll.print_list())
cll.insert_at_between(10111,100)
print(cll.count())
cll.print_list()
print()
print(cll.print_list())
# print()
print(cll.floyd())
# print(cll.reverse())