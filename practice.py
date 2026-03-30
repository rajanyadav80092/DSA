class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        return
    
    
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        return
    
    def print_forward(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("END")
    
    def backward_node(self):
        if self.head is None:
            print("list is empty")
            return
        prev=None
        curr=self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev
    
    def medium(self):
        if self.head is None:
            return "list is empty"
        
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    
    #sort all list
    # def sort(self):
    #     if self.head is None:
    #         return "list is empty"
    #     temp=self.head
    #     a=[]
    #     while temp:
    #         a.append(temp.data)
    #         temp=temp.next
    #     for i in range(1,len(a)):
    #         key=a[i]
    #         j=i-1
    #         while j>=0 and key<=a[j]:
    #             a[j+1]=a[j]
    #             j-=1
    #         a[j+1]=key
    #     return a
    
    def sortList(self,head):
        if self.head is None or self.head.next is None:
            return head
        slow=self.head
        fast=self.head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next #4
        slow.next=None #3-None
        left=self.sortList(head)
        right=self.sortList(mid)
        
        return self.merge(left,right)
    def merge(self,l1,l2):
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
    
    def reversekth(self,left,right):
        if self.head is None:
            return "list is empty"
        dummy=Node(0)
        dummy.next=self.head
        temp=dummy
        for _ in range(left-1):
            temp=temp.next #1
        curr=temp.next #2
        for _ in range(right-left):
            nxt=curr.next #3
            curr.next=nxt.next #2-4
            nxt.next=temp.next #3-2
            temp.next=nxt # 1-3
        dummy.next=self.head
        return dummy.next
    
    def midial_last(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        self.head=slow
        while slow:
            slow=slow.next
        return slow
    
    def remove(self,num):
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        curr=self.head
        while curr :
            if curr.data==num:
                while curr and curr.data==num:
                    curr=curr.next
                prev.next=curr
            else:
                prev=prev.next
                curr=curr.next
        dummy.next=self.head
        return self.head
               
            
                
ll=Linkedlist()
ll.insert_at_begining(6)
ll.insert_at_begining(6)
ll.insert_at_begining(6)
ll.insert_at_begining(6)
ll.insert_at_begining(6)
# ll.insert_at_begining(5)
# ll.insert_at_begining(4)
# ll.insert_at_begining(3)
# ll.insert_at_begining(2)
# ll.insert_at_begining(1)
ll.print_forward()
# ll.reversekth(2,4)
# ll.midial_last()
ll.remove(6)
ll.print_forward()
# print(ll.sortList())

        
        