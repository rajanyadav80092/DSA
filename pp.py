class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Circularlinkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
            return True
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        return True
    
    def insert_at_between(self,target_data,new_data):
        new_node=Node(new_data)
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next != self.head:
            if temp.data==target_data:
                next_node=temp.next
                temp.next=new_node
                new_node.prev=temp
                new_node.next=next_node
                next_node.prev=new_node
                return True
            temp=temp.next
        if temp.data==target_data:
            temp.next=new_node
            new_node.next=self.head
            self.head.prev=new_node
            new_node.prev=temp
            return True
        return "data is not found"
    
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
        new_node.prev=temp
        new_node.next=self.head
        self.head.prev=new_node
        return True
        
    
    def print_forward(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while True:
            print(temp.data,end=" ")
            temp=temp.next
            if temp==self.head:
                break
    
    def print_backward(self):
        if self.head is None:
            return "list is empty"
        temp=self.head.prev
        while True:
            print(temp.data,end=" ")
            temp=temp.prev
            if temp==self.head.prev:
                break
    
    def length_list(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        leng=1
        while temp.next != self.head:
            leng+=1
            temp=temp.next
        return leng
    
    def midium(self):
        if self.head is None:
            return "list is empty"
        slow=self.head
        fast=self.head
        while fast.next != self.head and fast.next.next!=self.head:
            fast=fast.next.next
            slow=slow.next
        return slow.data
    
    def give_reference(self,data):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next != self.head:
            if temp.data==data:
                return temp
            temp=temp.next
        if temp.data==data:
            return temp
        return None
    
    def delete_by_reference(self,node):
        #case 1
        if self.head is None or node is None:
            return "empty list node is None"
        #case 2
        if node is self.head and node.next is self.head:
            self.head=None
            return "only one node those are deleted"
        
        #case 3
        if node is self.head and node.next != self.head:
            prv=node.prev
            nxt=node.next
            prv.next=nxt
            nxt.prev=prv
            self.head=nxt
            return "head node is deleted"
        
        #case 4
        prev_node=node.prev
        nxt_node=node.next
        prev_node.next=nxt_node
        nxt_node.prev=prev_node
        return "midian or last node is deleted"
    
    def delete_node(self,data):
        if self.head is None:
            return "list is empty"
        temp=self.head
        if temp.data==data:
            if temp.next == self.head:
                self.head=None
                return f"{data} is deleted"
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            temp=None
            return f"{data} is deleted"
        temp=self.head 
        prev=None
        while temp.next != self.head and temp.data != data:
            prev=temp
            temp=temp.next
        if temp.data != data:
            return "data is Not found"
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        return f"{data} is deleted"
    
    def is_circular(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next != self.head:
            if temp is None:
                return False
            temp=temp.next
        return True
                
cll=Circularlinkedlist()
cll.insert_at_begining(1)
cll.insert_at_between(1,2)
cll.insert_at_end(3)
cll.print_backward()
print()
cll.print_forward()
print()
print(cll.length_list())
print(cll.midium())
n=cll.give_reference(1)
print(cll.delete_by_reference(n))
print(cll.delete_node(2))
cll.print_forward()
print(cll.is_circular())
                
            