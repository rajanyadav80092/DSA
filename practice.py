class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        return
    
    
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        return
    
    def print_forward(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("END")
    
    def backward_node(self):
        if self.head is None:
            print("list is empty")
            return
        prev=None
        curr=self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev
    
    def medium(self):
        if self.head is None:
            return "list is empty"
        
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
ll=Linkedlist()
ll.insert_at_begining(5)
ll.insert_at_begining(4)
ll.insert_at_begining(3)
ll.insert_at_begining(2)
ll.insert_at_begining(1)
ll.print_forward()
print(ll.medium())
ll.backward_node()
ll.print_forward()
        
        