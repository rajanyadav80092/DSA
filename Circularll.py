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
        while temp.next !=self.head:
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
        self.head=new_node
        
    def insert_at_between(self,target_data,new_data):
        new_node=Node(new_data)
        temp=self.head
        while temp.next !=self.head:
            if temp.data==target_data:
                next_node=temp.next
                temp.next=new_node
                new_node.next=next_node
                return
            temp=temp.next
        if temp.data == target_data:
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
    
    
    def print_list(self):
        if self.head == None:
            print("cll is empty")
            return
        temp=self.head
        while temp.next != self.head:
            print(f"{temp.data}",end=" ")
            temp=temp.next
        print(temp.data,end=" ")
            
        
    def is_circular(self):
        if self.head is None:
            return "list is empty"
        slow=self.head
        fast=self.head
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
            
            if slow is fast:
                return True
            
        return False
    
    def midial(self):
        if self.head is None:
            return "list is empty"
        slow=self.head
        fast=self.head
        while fast.next !=self.head and fast.next.next !=self.head:
            slow=slow.next
            fast=fast.next.next
        print("midial")
        return slow.data
    
    def giveReference(self,data):
        if self.head is None:
            return None
        temp=self.head
        while temp.next !=self.head:
            if temp.data==data:
                return temp
            temp=temp.next
        if temp.data==data:
            return temp
        return None
    
    def delete_reference(self,node):
        if node is None:
            return "list is empty or data incorrect"
        
        #case 2
        if self.head is node and node.next is self.head:
            self.head=None
            return "only one node those are deleted"
        
        #case 3
        if node is self.head:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=node.next
            self.head=node.next
            return "head node is deleted"
        
        #case 4
        prev=None
        temp=self.head
        while temp.next != self.head:
            if temp==node:
                nxt=temp.next
                prev.next=nxt
                return "midial node delete"
            prev=temp
            temp=temp.next
        if temp==node:
            nxt=temp.next
            prev.next=nxt
            return "last node delete"
        return "data not found"
    
    def delete_node(self,data):
        if self.head is None:
            return "list is empty"
        temp=self.head
        if temp.data==data:
            if temp.next is self.head:
                self.head=None
                return  f"{data} is deleted"
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            self.head=temp.next
            return f"{data} is deleted"
        prev=None
        temp=self.head
        while temp.next != self.head and temp.data != data:
            prev=temp
            temp=temp.next
        if temp.data != data:
            return "data is not correct"
        prev.next=temp.next
        return  f"{data} is delete midial or last node delete"
    
    def reverse(self):
        if self.head is None:
            return "list is empty"
        prev=None
        temp=self.head
        while temp.next != self.head:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
        if temp.next==self.head:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
            
        self.head=prev
        
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=self.head
        return
            
    def reverse(self):
        if self.head is None:
            return "list is empty"
        last=self.head
        while last.next != self.head:
            last=last.next
        
        prev=last
        temp=self.head
        while temp.next != self.head:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
        
        nxt=temp.next
        temp.next=prev
        prev=temp
        temp=nxt
        self.head=prev
        return
            
            
    
        
cll=CircularLinkedlist()
a=[11,100,101,110,10]
for i in a:
    cll.insert_at_end(i)
b=[111,222]
for j in b:
    cll.insert_at_beginning(j)
cll.print_list()
print()
# print(cll.delete_node(111))
# n=cll.giveReference(11)
# print(cll.delete_reference(n))
# print(cll.print_list())
cll.insert_at_between(100,1011)
print()
print("count")
print(cll.count())
cll.print_list()
print(cll.midial())
# print()
# print(cll.print_list())
print(cll.is_circular())
# # print()
cll.reverse()
cll.print_list()
print(cll.is_circular())