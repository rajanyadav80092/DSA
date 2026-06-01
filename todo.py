class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class Circularsinglylist:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
            return
        nxt_node=self.head.prev  #last node
        new_node.next=self.head
        self.head.prev=new_node
        new_node.prev=nxt_node
        nxt_node.next=new_node
        self.head=new_node
        return
    
    def insert_at_between(self,old_data,new_data):
        new_node=Node(new_data)
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next != self.head:
            if temp.data==old_data:
                nxt_node=temp.next
                temp.next=new_node
                new_node.prev=temp
                new_node.next=nxt_node
                nxt_node.prev=new_node
                return
            temp=temp.next
        if temp.data==old_data:
            nxt_node=temp.next
            temp.next=new_node
            new_node.prev=temp
            new_node.next=nxt_node
            nxt_node.prev=new_node
            return
        return "data is not found"
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
            return
        nxt_node=self.head.prev  #last
        nxt_node.next=new_node
        new_node.prev=nxt_node
        new_node.next=self.head
        self.head.prev=new_node
        return
    
    def print_forword(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        a=[]
        while temp.next != self.head:
            print(f"{temp.data}",end=" ")
            temp=temp.next
        print(f"{temp.data} ",end=" ")
        
    def delete_data(self,data):
        if self.head is None:
            return "list is empty"
        temp=self.head
        if temp.data==data:
            if temp.next is self.head:
                self.head=None
                return f"delete only one node {data}"
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            temp=None
            return f"{data} is deleted"
        
        prev=None
        temp=self.head
        while temp.next != self.head and temp.data !=data:
            prev=temp
            temp=temp.next
            
        if temp.data != data:
            return "data is not found"
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        return f"{data} is deleted"
    
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
    
    def delete_reference(self,node):
        if node is None or self.head is None:
            return "data not found or empty list"
        
        #case 2
        if self.head is node and node.next is node:
            self.head=None
            return "only one node those are delete"
        
        #case 3
        if self.head is node:
            prev=node.prev
            nxt=node.next
            prev.next=nxt
            nxt.prev=prev
            self.head=nxt
            return "head node is deleted"
        #case 4
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        return "midial or last node delete"
    
    def is_circular(self):
        if self.head is None:
            return "list is empty"
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow is fast:
                return True
        return False
    
    def midiam(self):
        if self.head is None:
            return "list is empty"
        slow=self.head
        fast=self.head
        while fast.next != self.head and fast.next.next != self.head:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    
            
    

cll=Circularsinglylist()
cll.insert_at_begining(10)
cll.insert_at_between(10,11)
cll.insert_at_end(12)
print(cll.delete_data(11))
# n=cll.give_reference(12)
# print(cll.delete_reference(n))
cll.print_forword()
print(cll.is_circular())
            
                
        


            