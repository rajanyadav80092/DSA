class Node:
    def __init__(self,data):
        self.prev=None
        self.next=None
        self.data=data
        
class Circulardoublylinked:
    def __init__(self):
        self.head =None
        
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
    
    def insert_at_between(self,target_data,new_data):
        new_node=Node(new_data)
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp.next != self.head:
            if temp.data==target_data:
                next_node=temp.next
                temp.next=new_node
                new_node.prev=temp
                new_node.next=next_node
                next_node.prev=new_node
                return
            temp=temp.next
        if temp.data==target_data:
            next_node=temp.next
            temp.next=new_node
            new_node.prev=temp
            new_node.next=next_node
            next_node.prev=new_node
            return
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
    
    def midium_node(self):
        if self.head is None:
            print("list is empty")
            return
        slow=self.head
        fast=self.head
        while fast.next != self.head and fast.next.next !=self.head:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    
    def length_node(self):
        if self.head is None:
            print("list is empty")
            return
        leng=1
        temp=self.head
        while temp.next != self.head:
            leng+=1
            temp=temp.next
        return leng
    
    def delete_node(self,data):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        if temp.data==data:
            if temp.next==temp:
                self.head=None
                print(f"deleted {data}")
                return
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            temp=None
            print(f"deleted : {data}")
            return
        temp=self.head
        prev=None
        while temp.next !=self.head and temp.data != data:
            prev=temp
            temp=temp.next
        if temp.data == data:
            prev.next=temp.next
            temp.next.prev=prev
            temp=None
            print(f"deleted {data}")
            return
        print("data is Not found")
        return
        
    def is_circular(self):
        if self.head is None:
            print("list is empty")
            return
        slow=self.head
        fast=self.head
        while fast.next != self.head:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                print("Circular")
                return
        print("Not Circular")
        return
    
    def get_reference(self,data):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp.next != self.head:
            if temp.data==data:
                return temp
            temp=temp.next
        if temp.data==data:
            return temp
        return None
    
    def delete_reference(self,node):
        #case 1
        if self.head is None or node is None:
            print("data not found or node is None")
            return
        
        #case2
        if self.head is node and node.next is node:
            self.head=None
            print("only one node those will be delete")
            return
        
        #case 3
        if self.head is node:
            last=self.head.prev
            self.head=self.head.next
            self.head.prev=last
            last.next=self.head
            print("head node will be deleted")
            return
        #case 4
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node
        print("middle or last node delete")
        return
    
    def swap_num(self,data):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp.next != self.head:
            if temp.data==data:
                left=temp.prev
                right=temp.next
                show=temp.next.next
                left.prev.next=right
                right.next=temp
                temp.next=left
                left.prev=temp
                left.next=show
                return
            temp=temp.next
        print("data is Not found")
        return
                
                
    
cll=Circulardoublylinked()
cll.insert_at_begining(1)
cll.insert_at_between(1,2)
cll.insert_at_end(3)
cll.insert_at_end(4)
cll.insert_at_end(5)
cll.print_backward()
print()
cll.print_forward()
print()
cll.swap_num(3)
cll.print_forward()
print()
print("midium",cll.midium_node())
print("length",cll.length_node())
cll.delete_node(1)
cll.print_forward()

print()
print(cll.is_circular())
n=cll.get_reference(3)
cll.delete_reference(n)
cll.is_circular()
                            
        
        