class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data
        
class circularDll:
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
        while temp.next!=self.head:
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
        self.head.prev=new_node
        new_node.prev=temp
        self.head=new_node
        return
    
    def insert_at_between(self,data,key):
        new_node=Node(key)
        if self.head is None:
            print("list is empty")
            return 
        temp=self.head
        while temp.next!=self.head:
            if temp.data==data:
                next_node=temp.next
                temp.next=new_node
                new_node.next=next_node
                new_node.prev=temp
                next_node.prev=new_node
                return
            temp=temp.next
        if temp.data == data:
            next_node=temp.next
            temp.next=new_node
            new_node.prev=temp
            new_node.next=next_node
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
        new_node.prev=temp
        new_node.next=self.head
        self.head.prev=new_node
        return
    
    def print_forword(self):
        if self.head is None:
            print("data is not found")
            return
        temp=self.head
        while True:
            print(temp.data,end=" ")
            temp=temp.next
            if temp==self.head:
                break
    def print_backword(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        temp=self.head.prev
        while True:
            print(temp.data ,end=" ")
            temp=temp.prev
            if temp==self.head.prev:
                break
    def middle_num(self):
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
        lengt=0
        temp=self.head
        while temp.next != self.head:
            lengt+=1
            temp=temp.next
        return f"length : {lengt+1}"
    
    def give_reference(self,data):
        if self.head is None:
            return
        temp=self.head
        while temp.next!= self.head:
            if temp.data == data:
                return temp
            temp=temp.next
        if temp.data == data :
            return temp
        return 
    
    def delete_reference(self,node):
        #case 1
        if self.head is None or node is None:
            print("node is none or data not found")
            return True
        #case 2
        if self.head.next==node and node.next==node:
            self.head=None
            print("head node is delete or only one node those deleted")
            return
        #case 3
        if node==self.head:
            last=self.head.prev
            self.head=self.head.next
            self.head.prev=last
            last.next=self.head
            print("head node is deleted")
            return
        #case 4 middle or last node deleted
        prev_node=node.prev
        next_node=node.next 
        prev_node.next=next_node
        next_node.prev=prev_node
        print("middle node is deletd")
        return           
    
    def delete_node(self,key):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        if temp.data == key:
            if temp.next==self.head:
                self.head=None
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next       
            temp.next.prev=last
            temp=None
            return f"{key} deleted"
        prev=None
        while temp.next != self.head and temp.data != key:
            prev=temp
            temp=temp.next
        if temp.data != key:
            print("data is not found")
            return
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        return f"deleted : {key}"
    
    def swap_num(self,target):
        if self.head is None:
            return "linked list is empty"
        temp=self.head
        while temp.next != self.head:
            if temp.data==target:
                left=temp.prev
                right=temp.next
                show=right.next
                left.prev.next=right
                right.prev=left.prev
                right.next=temp
                temp.next=left
                left.prev=temp
                left.next=show
                show.prev=left
                return
            temp=temp.next
        return "data not found"
                
            
    
                
    def is_circular(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head.prev
        if temp is None:
            return False
        return temp.next==self.head and self.head.prev==temp
            
cll=circularDll()
cll.insert_at_begining(1)
cll.insert_at_begining(2)
cll.insert_at_between(2,21)
cll.insert_at_begining(3)
cll.insert_at_end(33)
cll.print_forword()
print()
# cll.print_backword()
cll.swap_num(21)
print()
cll.print_forword()

print()
# print(cll.middle_num())
# # print(cll.index())
# print(cll.length())
# print(cll.delete_node(1))
# n=cll.give_reference(20)
# cll.delete_reference(n)
# print(cll.is_circular())
                
                
            