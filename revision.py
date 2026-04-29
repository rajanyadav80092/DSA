class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class Circulardoubly:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        new_node.prev=self.head.prev
        self.head.prev.next=new_node
        return
    
    def insert_at_between(self,old_data,data):
        new_node=Node(data)
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next!=self.head:
            if temp.data==old_data:
                next_node=temp.next
                temp.next=new_node
                new_node.prev=temp
                new_node.next=next_node
                next_node.prev=new_node
                return
            temp=temp.next
        if temp.data==old_data:
            next_node=temp.next
            temp.next=new_node
            new_node.prev=temp
            new_node.next=next_node
            next_node.prev=new_node
            return 
        return "data is Not found"
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
            return 
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        new_node.next=self.head
        self.head.prev=new_node
        return 
    def print_forward(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next!=self.head:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data,end=" ")
    def print_backward(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        curr=temp
        while curr!=self.head:
            print(curr.data,end=" ")
            curr=curr.prev
        print(curr.data,end=" ")
        
    def midium(self):
        if self.head is None:
            return "list is empty"
        slow=self.head
        fast=self.head
        while fast.next != self.head and fast.next.next != self.head:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    
    def length(self):
        if self.head is None:
            return "list is empty"
        lengt=1
        curr=self.head
        while curr.next!= self.head:
            curr=curr.next
            lengt+=1
        return lengt
    
    def give_reference(self,data):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next!=self.head:
            if temp.data==data:
                return temp
            temp=temp.next
        if temp.data==data:
            return temp
        return None
    
    def delete_by_reference(self,node):
        #case 1
        if self.head is None or node is None:
            return "list is none or Node data Not found"
        
        #case2
        if self.head is node or node.next is node:
            self.head=None
            return "Only on node those are delete"
        
        #case 3
        if self.head is node:
            last=self.head.prev
            last.next=self.head.next
            self.head.next.prev=last
            self.head=self.head.next
            return "head node is delete"
        
        #case 4
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        return "middle or last node is delete"
    
    def delete_node(self,data):
        if self.head is None:
            return "list is empty"
        temp=self.head
        if temp.data==data:
            if temp.next is self.head:
                self.head=None
                return "only one node those are deleted"
            last=self.head
            while last.next!=self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            temp=None
            return f"deleted {data} is head data"
        prev=None
        temp=self.head
        while temp.next !=self.head and temp.data!=data:
            prev=temp
            temp=temp.next
        if temp.data!=data:
            return "data is Not found"
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        return f"{data} is delete"
    
    def removenth(self,n):
        temp=self.head
        slow=self.head
        for _ in range(n):
            temp=temp.next
        while temp.next != self.head:
            slow=slow.next
            temp=temp.next
        slow.next=slow.next.next #3-5
        temp.prev=slow
        
        return self.head
    
            
            
    def is_circular(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        curr=self.head
        while True:
            if temp.next==None:
                return False
            temp=temp.next.next
            curr=curr.next
            if curr==temp:
                return True
            
cll=Circulardoubly()
cll.insert_at_begining(1)
cll.insert_at_between(1,2)
cll.insert_at_end(3)
cll.insert_at_end(4)
cll.insert_at_end(5)
cll.print_forward()
# print(cll.midium())
# n=cll.give_reference(3)
# print(cll.delete_by_reference(n))
# print(cll.length())
# print(cll.delete_node(2))
# cll.print_forward()
cll.removenth(2)
print()
# cll.print_backward()
cll.print_forward()
print(cll.is_circular())
