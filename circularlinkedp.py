class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class circular:
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
                new_node.prev=temp
                new_node.next=next_node
                next_node.prev=new_node
                return
            temp=temp.next
        if temp.data==data:
            temp.next=new_node
            new_node.prev=temp
            new_node.next=self.head
            self.head.prev=new_node
            return
        return print("data is not found")
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
            return
        temp=self.head
        while temp.next!= self.head:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        new_node.next=self.head
        self.head.prev=new_node
    def midiam(self):
        slow=self.head
        fast=self.head
        while fast.next != self.head and fast.next.next != self.head:
            slow=slow.next 
            fast = fast.next.next
        return print(slow.data)
    def index(self):
        lent=0
        temp=self.head
        while temp.next != self.head:
            lent+=1
            temp=temp.next
        return print("index", lent)
    
    def lenth(self):
        ind=1
        temp=self.head
        while temp.next !=self.head:
            ind+=1
            temp=temp.next
        return print("length",ind)
        
    def print_forward(self):
        if self.head is None:
            return print("list is empty")
        temp=self.head
        while temp.next != self.head:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data,end=" ")
        
    def delete_node(self,data):
        if self.head is None:
            return print("list is empty")
        temp=self.head
        if temp.data==data:
            if temp.next is self.head:
                self.head=None
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            return print(f"data is remove {data}")
        prev=None
        while temp.next != self.head and temp.data!=data:
            prev=temp
            temp=temp.next
        if temp.data != data :
            return print("data is not found")
        prev.next=temp.next
        temp.next.prev=prev
        return print(data,"is remove")
    
    def print_backword(self):
        if self.head is None:
            return print("list is empty")
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        pro=self.head.prev
        while True:
            print(pro.data,end=" ")
            pro=pro.prev
            if pro==self.head.prev:
                break
            
    def circular_list(self):
        if self.head is None:
            return print("list is empty")
        slow=self.head
        fast=self.head
        while True:
            if fast.next is None:
                return print("not circular")
            fast=fast.next
            slow=slow.next
            if slow == fast:
                return print("circular link list")
        
            
cll=circular()
cll.insert_at_between(2,22)
# cll.insert_at_begining(10)
# cll.insert_at_begining(20)
# cll.insert_at_between(20,11)
# cll.insert_at_end(12)
# cll.insert_at_begining(100)
# cll.insert_at_begining(123)
# cll.midiam()
# cll.print_forward()
# print()
# cll.delete_node(123)
# print()
# cll.print_forward()
# print()
# cll.print_backword()
# print()
# cll.index()
# cll.lenth()
# cll.circular_list()
# print()
        
        
        