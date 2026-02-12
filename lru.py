class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class Circulardoubly:
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):
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
        self.head=new_node
        return
    
    def insert_at_between(self,data,key):
        new_node=Node(key)
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp.next != self.head:
            if temp.data==data:
                next_node=temp.next
                temp.next=new_node
                new_node.next=next_node
                next_node.prev=new_node
                new_node.prev=temp
                return
            temp=temp.next
        if temp.data==data:
            next_node=temp.next
            new_node.next=next_node
            temp.next=new_node
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
        new_node.prev=temp
        new_node.next=self.head
        self.head.prev=new_node
        return
    
    def print_forward(self):
        if self.head is None:
            print("list is empty")
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
            if temp== self.head.prev:
                break
    
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
    
    def delete_reference(self,node):
        # case 1 node is none 
        if self.head is None or node is None:
            print("list is None")
            return
        
        #case 2 if only one node
        if self.head is node and node.next == node:
            self.head =None
            print("only one node or delete")
            return
        
        #caase 3 head node is delete
        if node==self.head :
            last=self.head.prev
            self.head=self.head.next  
            last.next=self.head
            self.head.prev=last
            print("delete head node")
            return
         #case 4
        prev_node=node.prev
        nxt_node=node.next
        
        prev_node.next=nxt_node
        nxt_node.prev=prev_node
        print("delete middle node")
        return
    
    def delete_node(self,data):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        if temp.data == data:
            if temp.next == temp:
                self.head = None
                print(f"{data} is deleted")
                return
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            temp=None
            print(f"{data} is deleted")
            return
        prev=None
        temp=self.head
        while temp.next != self.head and temp.data != data:
            prev=temp
            temp=temp.next
        if temp.data != data:
            print("data is not found")
            return
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        print(f"{data} is deleted")
        return
    
    def middle_node(self):
        if self.head is None:
            print("list is empty")
            return
        slow=self.head
        fast=self.head
        while fast.next != self.head and fast.next.next !=self.head:
             slow=slow.next
             fast=fast.next.next
        return slow.data
    
    def index_node(self):
        if self.head is None:
            print("list is empty")
            return
        idx=0
        temp=self.head
        while temp.next != self.head:
            idx+=1
            temp=temp.next
        print("index : " ,idx) 
        return
    
    def length(self):
        if self.head is None:
            print("list is empty")
            return
        leng=1
        temp=self.head
        while temp.next != self.head:
            leng+=1
            temp=temp.next
        print("length : ",leng)
        return
    
    def josephus(self,data,k):
        if self.head is None:
            self.head=Node(1)
        temp=self.head
        for i in range(2,data+1):
            temp.next=Node(i)
            temp.prev=temp
            temp=temp.next
        temp.next=self.head
        self.head.prev=temp
        
        prev=None
        temp=self.head
        while temp.next != temp:
            for _ in range(k-1):
                prev=temp
                temp=temp.next
            prev.next=temp.next
            temp=temp.next
        return temp.data
    
    def is_circular(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head.prev
        if temp is None:
            return False
        return temp.next==self.head and self.head.prev==temp
    
    def is_palindrome(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        paridrome=[]
        while temp.next != self.head:
            paridrome.append(temp.data)
            temp=temp.next
        paridrome.append(temp.data)
        if paridrome==paridrome[::-1]:
            return True
        return False
             
cll=Circulardoubly()
cll.insert_at_beginning(1)
cll.insert_at_between(1,2)
cll.insert_at_end(1)
cll.insert_at_beginning(4)
cll.insert_at_between(4,5)
cll.insert_at_end(6)
cll.print_forward()
print()
cll.print_backward()
print()
cll.length()
print(cll.middle_node())
cll.index_node()
n=cll.get_reference(6)
cll.delete_reference(n)
cll.delete_node(2)
print()
print(cll.is_circular())
cll.is_palindrome()
print(cll.josephus(10,3))              
                  
            
        