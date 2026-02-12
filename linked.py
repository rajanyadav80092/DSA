class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class Doublylinkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        
    
    def insert_at_between(self,target,new_target):
        new_node=Node(new_target)
        if self.head is None:
            print("list is empty")
            return 
        temp=self.head
        while temp.next:
            if temp.data==target:
                next_node=temp.next
                temp.next=new_node
                new_node.prev=temp
                new_node.next=next_node
                next_node.prev=new_node
                return 
            temp=temp.next
        if temp.data==target:
            temp.next=new_node
            new_node.prev=temp
            return 
        print("data is not found")
        return 
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        return
    
    def print_forward(self):
        if self.head is None:
            print("list is empty")
            return 
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("None")
        return
    
    def print_backward(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp=temp
        while temp.prev:
            print(temp.data,end=" ")
            temp=temp.prev
        print(temp.data,end=" ")
        return
   
    def midian(self):
        if self.head is None:
            print("list is empty")
            return
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    
    def length(self):
        if self.head is None:
            print("list is empty")
        temp=self.head
        leng=0
        while temp:
            leng+=1
            temp=temp.next
        return leng
    
    def delete_node(self,data):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        if temp.data==data:
            if temp.next is None:
                self.head=None
                print(f"deleted {data}")
                return 
            self.head=temp.next
            temp.next.prev=None
            print(f"deleted {data}")
            return
        prev=None
        temp=self.head
        while temp and temp.data!= data:
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
        
    def is_circular(self):
        if self.head is None:
            print("list is empty")
            return
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                print("circular")
                return
        print("not circular")
        return
    
    def get_reference(self,data):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp:
            if temp.data==data:
                return temp
            temp=temp.next
        return None
    
    def delete_by_reference(self, node):

    # Case 1: empty list or invalid node
        if self.head is None or node is None:
            print("Invalid deletion")
            return

    # Case 2: only one node in list
        if self.head == node and node.next is None:
            self.head = None
            print("Only node deleted")
            return

    # Case 3: deleting head node
        if node == self.head:
            self.head = node.next
            self.head.prev = None
            print("Head node deleted")
            return

    # Case 4: middle or last node
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node

        if next_node:
            next_node.prev = prev_node

        print("Node deleted by reference")
        return

        
dll=Doublylinkedlist()
dll.insert_at_begining(1)
dll.insert_at_end(2)
dll.insert_at_begining(3)
dll.insert_at_between(2,4)
dll.print_forward()

dll.delete_node(3)
print(dll.print_backward())
print(dll.midian())
print(dll.length())
dll.is_circular()
        
            
        
        
    