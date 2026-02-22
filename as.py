class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data

class Circulardoublylinkedlist:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self,data):
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
        self.head=new_node
        return
    
    def insert_at_between(self,target,new_data):
        new_node=Node(new_data)
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp.next != self.head:
            if temp.data == target:
                next_node=temp.next
                temp.next=new_node
                new_node.prev=temp
                new_node.next=next_node
                next_node.prev=new_node
                return
            temp=temp.next
        if temp.data == target:
            next_node=temp.next
            temp.next=new_node
            new_node.prev=temp
            new_node.next=next_node
            next_node.prev=new_node
            return
        print("target is not found")
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
        new_node.prev=temp
        new_node.next=self.head
        self.head.prev=new_node
        return
    
    def print_forward(self):
        if self.head is None:
            print("List is empty")
            return
        temp=self.head
        while temp.next != self.head:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data,end=" ")
        return
    
    def print_backward(self):
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
            if temp == self.head.prev:
                break
    
    def is_circular(self):
        if self.head is None:
            print("list is empty")
            return 
        temp=self.head.prev
        return temp.next == self.head 
        
    def midium(self):
        if self.head is None:
            print("list is empty")
            return
        slow=self.head
        fast=self.head
        while fast.next != self.head and fast.next.next!=self.head:
            fast=fast.next.next
            slow=slow.next
        return slow.data
    
    def length(self):
        if self.head is None:
            print("list is empty")
            return
        leng=1
        temp=self.head
        while temp.next != self.head:
            leng+=1
            temp=temp.next
        return leng
    
    def get_reference(self,data):
        if self.head is None:
            print("List is empty")
            return
        temp=self.head
        while temp.next != self.head:
            if temp.data == data:
                return temp
            temp=temp.next
        if temp.data == data:
            return temp
        return None
    
    def delete_reference(self,node):
        #case 1 
        if self.head is None or node is None:
            print("list is empty or node is not found")
            return
        
        #case 2
        if self.head is node and node.next == self.head:
            self.head=None
            print("only one node that delete")
            return
        
        #case 3
        if self.head is node:
            last=self.head.prev
            self.head=self.head.next
            self.head.prev=last
            last.next=self.head
            print("head node only that delete")
            return
        
        #case 4
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node
        print("midial node or last node delete")
        return
            
    def delete_node(self,data):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        if temp.data==data:
            if temp.next == self.head:
                self.head=None
                print(f"{data} is delete")
                return
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            temp=None
            print(f"{data} is deleted")
            return
        temp=self.head
        prev=None
        while temp.next != self.head and temp.data != data:
            prev=temp
            temp=temp.next
        if temp.data != data:
            print("data is not found")
            return
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        print(f"{data} is delete")
        return
            
        
    
cll=Circulardoublylinkedlist()
cll.insert_at_begining(1)
cll.insert_at_between(1,2)
cll.insert_at_end(3)
cll.print_forward()
print()
cll.print_backward()
print()
print(cll.length())

print(cll.midium())
print(cll.is_circular())
n=cll.get_reference(2)
cll.delete_reference(n) 
cll.print_forward()  
print()
cll.delete_node(1)
print()
cll.print_forward()
            
    
        
            
                
                