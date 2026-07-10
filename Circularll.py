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
        if self.head is None or node is None:
            return "list is empty or node is not found"
        
        if self.head is node and node.next is node:
            self.head=None
            return "only one node those are deleted"
        
        if self.head is node:
            temp=self.head
            while temp.next !=self.head:
                temp=temp.next
            nxt=node.next
            temp.next=nxt
            self.head=nxt
            return "head node is deleted"
        
        
        temp=self.head
        prev=None
        while temp !=node:
            prev=temp
            temp=temp.next
        prev.next=temp.next
        return "last node is deleted"
        
        
        
    def delete_node(self,data):
        if self.head is None:
            return  "list is emtpy"
        temp=self.head
        if temp.data==data:
            if temp.next is self.head:
                self.head=None
                return "only one node those are deleted"
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            self.head=temp.next
            return "head node is delete"
        prev=None
        temp=self.head
        while temp.next != self.head and temp.data !=data:
            prev=temp
            temp=temp.next
        if temp.data ==data:
            prev.next=temp.next
            return "middle or last node is deleted"
        return "data is not found"
    
    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return self.head
        prev=None
        old_node=self.head
        temp=self.head
        while temp.next !=self.head:
            curr=temp.next
            temp.next=prev
            prev=temp
            temp=curr
            
        temp.next=prev
        prev=temp
        self.head=prev
        old_node.next=self.head
        return self.head
        # temp=self.head
        # arr=[]
        # while temp.next != self.head:
        #     arr.append(temp.data)
        #     temp=temp.next
        # arr.append(temp.data)
        # dummy=Node(0)
        # temp=dummy
        # while arr:
        #     a=arr.pop()
        #     temp.next=Node(a)
        #     temp=temp.next
        # self.head=dummy.next
        # temp.next=self.head
        # return self.head
        
            
    def pr(self):
        temp=self.head
        while temp.next != self.head:
            print(f"{temp}:{temp.data}")
            temp=temp.next
        print("END") 
    
        
cll=CircularLinkedlist()
a=[1,2,3,4,5]
for i in a:
    
    cll.insert_at_end(i)
# cll.insert_at_beginning(20)
# n=cll.giveReference(20)
# print(cll.delete_reference(n))

# for i in a:
#     cll.insert_at_end(i)
# b=[111,222]
# for j in b:
#     cll.insert_at_beginning(j)
cll.print_list()
print()
print(cll.reverse())
# print(cll.delete_node(222))
cll.print_list()
# n=cll.giveReference(11)
# print(cll.delete_reference(n))
# print(cll.print_list())
# cll.insert_at_between(100,1011)
# print()
# print("count")
# print(cll.count())
# cll.print_list()
# print(cll.midial())
# # print()
# # print(cll.print_list())
print(cll.is_circular())
# # # print()
# cll.reverse()
# cll.print_list()
# print(cll.is_circular())