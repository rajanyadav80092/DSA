class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        return 
    
    def insert_at_between(self,old_data,data):
        new_node=Node(data)
        if self.head is None:
            return "list is emtpy"
        temp=self.head
        while temp:
            if temp.data==old_data:
                nxt=temp.next
                temp.next=new_node
                new_node.next=nxt
                return 
            temp=temp.next
    
    def insert_at_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        return 
    
    def reverse_list(self):
        if self.head is None:
            return "list is empty"
        prev=None
        curr=self.head
        while curr:
            nxt=curr.next  #2
            curr.next=prev #1-None
            prev=curr  #none me 1
            curr=nxt   #2
        self.head=prev
        return prev
    
    def detect_cycle(self):
        if self.head is None:
            return "list is empty"
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow.data==fast.data:
                return True
        return False #agar list cycle nahi to None hoga na isliye aisa logic likha hu 
    def remove_last_nth(self,n):
        if self.head is None:
            return "list is empty"
        dummy=Node(0)
        dummy.next=self.head
        slow=dummy
        fast=dummy
        for _ in range(n):
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        self.head=dummy.next
        return dummy.next
    def print_forward(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("END")
    
    def midial(self):
        if self.head is None:
            return "list si empty"
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    
    def merge(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy=Node(0)
        temp=dummy
        while l1 and l2:
            if l1.data<l2.data:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
        if l1:
            temp.next=l1
        if l2:
            temp.next=l2
        return dummy.next
    
    def swap_node_start_end_kth(self,n):
        if self.head is None:
            return "list is empty"
        slow=self.head
        fast=self.head
        for _ in range(n-1):
            fast=fast.next
        first=fast
        while fast.next:
            slow=slow.next
            fast=fast.next
        second=slow
        first.data,second.data=second.data,first.data
        return self.head
    
    def delete_last(self,n):
        if self.head is None:
            return "list is empty"
        arr=[]
        temp=self.head
        while temp:
            arr.append(temp.data)
            temp=temp.next
        c=len(arr)-n
        dummy=Node(0)
        temp=dummy
        for i in range(len(arr)):
            if i==c:
                continue
            temp.next=Node(arr[i])
            temp=temp.next
        self.head=dummy.next
        return dummy.next
    
    def remove_last_nth(self,n):
        if self.head is None:
            return "list is empty"
        dummy=Node(0)
        dummy.next=self.head
        slow=dummy
        fast=self.head
        for _ in range(n-1):
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next
    def midiallast(self):
        if self.head is None:
            return "list is empty"
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        self.head=slow
        return slow
    def remove_num(self,num):
        dummy=Node(0)
        prev=dummy
        dummy.next=self.head
        curr=self.head
        while curr:
            if curr.data==num:
                while curr and curr.data==num:
                    prev.next=curr.next
                    curr=curr.next
            else:
                prev=prev.next
                curr=curr.next
        return prev.next
ll=LinkedList()
ll.insert_at_begining(1)
ll.insert_at_between(1,2)
ll.insert_at_end(3)
ll.insert_at_between(3,3)
ll.insert_at_between(3,3)
ll.insert_at_end(4)
ll.insert_at_end(5)
# ll.reverse_list()
# ll.remove_last_nth(2)
# print(ll.midial())
# ll.swap_node_start_end_kth(2)
# ll.midiallast()
# ll.remove_num(3)
ll.print_forward()
ll.remove_last_nth(2)
ll.print_forward()

        