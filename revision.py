class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head == None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr =next_node
        self.head=prev
    def count(self):
        len=0
        temp=self.head
        while temp:
            len+=1
            temp=temp.next
        return len
    
    def middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    def search(self,key):
        temp=self.head
        while temp:
            if temp.data==key:
                return True
            temp=temp.next
        return "not found key"
    
    def delete_node(self,key):
        temp=self.head
        
        if temp is not None and temp.data==key:
            self.head=temp.next
            temp=None
            return
        prev=None
        while temp is not None and temp.data!=key:
            prev=temp
            temp=temp.next
        if temp is None:
            print("value is not found")
            return
        prev.next=temp.next
        temp=None
            
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("None")
    
    def swap_node(self):
        if self.head is None:
            return "list is empty"
        dummy=Node(0)
        dummy.next=self.head
        
        prev=dummy
        while prev.next and prev.next.next:
            first=prev.next
            second=first.next
            
            #swap
            first.next=second.next
            second.next=first
            prev.next=second
            
            prev=first
        self.head=dummy.next
        return dummy.next   
    def swap_kth_node(self,k):
        if self.head is None:
            return "list is empty"
        dummy=Node(0)
        dummy.next=self.head
        
        prev=dummy
        while True:
            kth=prev
            for _ in range(k):
                kth=kth.next
                if not kth:
                    self.head=dummy.next
                    return dummy.next
            next_node=kth.next
            prev_node=next_node
            
            curr=prev.next
            while curr!= next_node:
                temp=curr.next #2 #3 #4
                curr.next=prev_node #1-4 #2-1 #3-2
                prev_node=curr #1 #2 #3
                curr=temp #2 #3 #4
            temp=prev.next #1
            prev.next=kth #3
            prev=temp #1
                
                
            
ll=Linkedlist()
ll.insert_at_beginning(10)
ll.insert_at_end(12)
ll.insert_at_beginning(101)
ll.insert_at_end(121)
ll.insert_at_beginning(102)
ll.insert_at_end(122)
ll.insert_at_beginning(103)
ll.insert_at_end(123)
ll.print_list()
ll.reverse()
ll.print_list()
print(ll.search(123))
print(ll.count())
print(ll.middle())
ll.delete_node(103)
ll.print_list()
ll.swap_node()
print("swap")
ll.print_list()
print("swap_target")
ll.swap_kth_node(3)
ll.print_list()

                 