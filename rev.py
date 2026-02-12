class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class CircularDoublylinkedlist:
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
        new_node.prev=temp
        self.head=new_node
        return
    
    def insert_at_between(self,search,target):
        new_node=Node(target)
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next != self.head:
            if temp.data== search:
                next_node=temp.next
                temp.next=new_node
                new_node.prev=temp
                new_node.next=next_node
                next_node.prev=new_node
                return 
            temp=temp.next
        if temp.data == search:
            next_node=temp.next
            temp.next=new_node
            new_node.next=next_node
            new_node.prev=temp
            next_node.prev=new_node
            return
        print("data is not found")
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
        self.head.prev=new_node
        new_node.prev=temp
        return
    
    def print_forward(self):
        if self.head is None:
            print("list is empty")
            return 
        temp=self.head
        while True:
            print(temp.data,end=" ")
            temp=temp.next
            if temp==self.head:
                break
        
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
            if temp==self.head.prev:
                break
    
    def middle_value(self):
        if self.head is None:
            print("list is empty")
            return
        fast=self.head
        slow=self.head
        while fast.next != self.head and fast.next.next !=self.head:
            fast=fast.next.next
            slow=slow.next
        return slow.data
    
    def length(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        leng=1
        while temp.next != self.head:
            temp=temp.next
            leng+=1
        return leng
    
    def delete_node(self,data):
        if self.head is None:
            print("list is empty")
            return 
        temp=self.head
        if temp.data==data:
            if temp.next == temp:
                self.head=None
                print(f"deleted : {data}")
                return 
            last=self.head
            while last.next!= self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            temp=None
            print(f"deleted {data}")
            return 


        temp=self.head
        prev=None
        while temp.next !=self.head and temp.data != data:
            prev=temp
            temp=temp.next
        if temp.data != data:
            print("data is Not found")
            return
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        print(f"deleted {data}")
        return
    
    def get_reference(self,data):
        if self.head is None:
            print("list is empty")
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
            print("node is None or empty list")
            return
        
        #case 2 
        if self.head == node and node.next == node:
            self.head=None
            print("only one node those are deleted")
            return
        #case 3
        if node==self.head :
            last=self.head.prev
            self.head=self.head.next
            last.next=self.head
            self.head.prev=last
            print("head node is deleted")
            return
        #case 4
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node
        print("middle or last node deleted")
        return 
            
    def is_circular(self):
        if self.head is None:
            print("list is empty")
            return
        return self.head.prev.next==self.head
    
    def josephus(self,data,k):
        if self.head is None:
            self.head=Node(1)
        temp=self.head
        for i in range(2,data+1):
            temp.next=Node(i)
            temp=temp.next
        temp.next=self.head
        
        prev=None
        temp=self.head
        while temp.next != temp:
            for _ in range(0,k-1):
                prev=temp
                temp=temp.next
            prev.next=temp.next
            temp=temp.next
        return temp.data
            
            
cll=CircularDoublylinkedlist()
cll.insert_at_begining(1)
cll.insert_at_between(1,2)
cll.insert_at_end(3)
cll.insert_at_begining(4)
cll.insert_at_between(4,5)
cll.insert_at_end(6)
cll.print_forward()
print()
cll.print_backward()
print()
cll.delete_node(2)
print(cll.middle_value())
print(cll.length())
n=cll.get_reference(3)
cll.delete_reference(n)
print(cll.is_circular())
print(cll.josephus(7,3))
            