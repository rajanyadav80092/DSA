class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        
    def insert_at_between(self,data,key):
        new_node=Node(key)
        temp=self.head
        while temp.next:
            if temp.data == data :
                next_node=temp.next
                temp.next=new_node
                new_node.next=next_node
                return
            temp=temp.next
        if temp.next is None and temp.data is data:
            temp.next=new_node
            return
        print("data is not found")
        return
            
                
        
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev
        
    def count(self):
        length=0
        temp=self.head
        while temp:
            temp=temp.next
            length+=1
        return length
    
    def middle(self):
        fast=self.head
        slow=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    
    def search(self,key):
        temp=self.head
        len=0
        while len<=self.count():
            len+=1
            if temp.data == key:
                return len,key
            temp=temp.next
        return -1
        
    def delete(self,key):
        temp=self.head
        if temp is not None and temp.data == key:
            self.head=temp.next
            temp=None
            return 
        prev=None
        while temp is not None and temp.data!=key:
            prev=temp
            temp=temp.next
        if temp is None:
            print("value not found")
            return 
        prev.next = temp.next
        temp=None
   
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ⇉ " )
            temp=temp.next
        print("None")
        
ll=Linkedlist()
# ll.insert_at_beginning(12)
ll.insert_at_beginning(13)
ll.insert_at_end(20)
ll.insert_at_beginning(14)
ll.insert_at_end(21)
ll.insert_at_end(22)
ll.insert_at_end(23)
ll.insert_at_between(21,122)
# print(ll.search(23))
ll.print_list()
# print(ll.middle())
# ll.reverse()
# ll.print_list()
# ll.delete(22)
# ll.print_list()
