class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

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
        temp=self.head.prev
        temp.next=new_node
        new_node.prev=temp
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    
    def insert_at_between(self,target_data,new_data):
        new_node=Node(new_data)
        if self.head is None:
            return "list is empty"
        temp=self.head
        while True:
            if temp.data==target_data:
                nxt=temp.next
                temp.next=new_node
                new_node.prev=temp
                nxt.prev=new_node
                new_node.next=nxt
                return
            temp=temp.next
            if temp==self.head:
                break
        print("target not found")
        return 
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
            return
        temp=self.head.prev
        temp.next=new_node
        new_node.prev=temp
        new_node.next=self.head
        self.head.prev=new_node
        return 
    
    def print_forward(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next != self.head:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data,end=" ")
    
    def print_backward(self):
        if self.head is None:
            return "list is empty"
        temp=self.head.prev
        while temp !=self.head:
            print(temp.data,end=" ")
            temp=temp.prev
        print(temp.data,end=" ")
        
    def midium(self):
        if self.head is None:
            return "list is empty"
        slow=self.head
        fast=self.head
        while fast.next != self.head and fast.next.next != self.head:
            fast=fast.next.next
            slow=slow.next
        return slow.data
    
    def length(self):
        if self.head is None:
            return "list is empty"
        lengt=1
        temp=self.head
        while temp.next != self.head:
            lengt+=1
            temp=temp.next
        return lengt
    
    def give_refrence(self,data):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while True:
            if temp.data == data:
                return temp
            temp=temp.next
            if temp == self.head:
                break
            
        return None
    
    def delete_by_refrence(self,n):
        #case 1
        if self.head is None or  n is None:
            print("list is None or data is Not found ")
            return
        #case 2
        if self.head==n and  n.next is n:
            self.head=None
            print("only one node those are deleted")
            return
        #case 3
        if self.head==n :
            last=self.head.prev
            last.next=self.head.next
            self.head.next.prev=last
            self.head=self.head.next
            print("first node is deleted")
            return
        #case 4
        prev=n.prev
        nxt=n.next
        prev.next=nxt
        nxt.prev=prev
        print("midium or last node is deleted")
        return

    def deleted_node(self,data):
        if self.head is None:
            print("list is empty")
            return 
        temp=self.head
        if temp.data==data:
            if temp.next == self.head:
                self.head=None
                print(f"{data} is deleted")
                return 
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            temp=None
            print(f"{data} is remove")
            return 
        prev=None
        temp=self.head
        while temp.next != self.head and temp.data != data:
            prev=temp
            temp=temp.next
        if temp.data!= data:
            print("data is not found")
            return
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        print(f"{data} is deleted")
        return
    
    def is_circular(self):
        if self.head is None:
            return False
        temp=self.head.next
        while temp and temp.next != self.head:
            temp=temp.next
        return temp.next==self.head
            
                
                 
            
    
cll=Circulardoublylinkedlist()
cll.insert_at_begining(1)
cll.insert_at_between(1,2)
cll.insert_at_end(3)
print(cll.midium())
print(cll.length())
n=cll.give_refrence(1)
cll.delete_by_refrence(n)
print(cll.is_circular())
cll.print_forward()
        
    