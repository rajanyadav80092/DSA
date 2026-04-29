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
    #time cp=omplexity O(1)
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    
    #time complexity O(n) space O(1)
    
    def reverse_list(self):
        if self.head is None:
            return "list is empty"
        curr=self.head
        prev=None
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev
        return prev
    
    #time complexity O(n) and space complexity O(1)
       
    def middle_node(self):
        if self.head is None:
            return "list is empty"
        fast=self.head
        slow=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow.data 
    
    #time complexity O(n) space complexity (1)
    def is_cycle(self):
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
    
    #time complexity O(n)
    
    #question 3
    def remove_end(self,k):
        if self.head is None:
            return "list is empty"
        arr=[]
        temp=self.head
        while temp:
            arr.append(temp.data)
            temp=temp.next
        l=len(arr)
        n=l-k
        dummy=Node(0)
        curr=dummy
        for i in range(l):
            if i==n:
                continue
            curr.next=Node(arr[i])
            curr=curr.next
        self.head=dummy.next
        return self.head
    
    #this is not optimal solution this is brute force time O(n) space O(n)
    
        
    
    def remove_nth_end(self,k):
        if self.head is None:
            return "list is empty"
        fast=self.head
        slow=self.head
        
        for i in range(k+1):
            fast=fast.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return self.head
    
    #time complexity O(n) space complexity O(1)
            
    def merge(self,l1,l2):
        dummy=Node(0)
        dummy.next=self.head
        temp=dummy
        
        while l1 and l2:
            if l1.data<=l2.data:
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
        self.head=dummy.next
        return self.head
    
    #time complexity O(n) space O(1)
                
    def odd_even(self):
        if self.head is None:
            return "list is empty"
        even=[]
        odd=[]
        temp=self.head
        while temp:
            if temp.data%2==0:
                even.append(temp.data)
            else:
                odd.append(temp.data)
            temp=temp.next
        return even+odd
    def even_to_even(self):
        if self.head is None:
            return "list is empty"
        even=[]
        odd=[]
        temp=self.head
        while temp:
            if temp.data%2==0:
                even.append(temp.data)
            else:
                odd.append(temp.data)
            temp=temp.next
        n=len(even)+len(odd)
        e,o=0,0
        even.sort()
        odd.sort(reverse=True)
        a=[]
        for i in range(n):
            if i%2==0:
                a.append(even[e])
                e+=1
            else:
                a.append(odd[o])
                o+=1
        dummy=Node(0)
        curr=dummy
        for i in range(len(a)):
            curr.next=Node(a[i])
            curr=curr.next
        self.head=dummy.next
        return dummy.next
        
    
    #start
    def odd_than_even(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        even=[]
        odd=[]
        while temp:
            if temp.data%2==0:
                even.append(temp.data)
            else:
                odd.append(temp.data)
            temp=temp.next
        
        a=odd+even
        n=len(a)
        dummy=Node(0)
        curr=dummy
        for i in range(n):
            curr.next=Node(a[i])
            curr=curr.next
        self.head=dummy.next
        return self.head
    
    #this is not optimal solution time and space both complexity O(n)
            
    def swap_node(self):
        if self.head is None:
            return "list is empty"
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        while prev.next and prev.next.next:
            first=prev.next  #1
            second=first.next   #2
            
            #swap
            first.next=second.next
            second.next=first
            prev.next=second
            prev=first
        self.head=dummy.next
        return dummy.next
    
    def reversenth(self,left,right):
        if self.head is None:
            return "list is empty"
        dummy=Node(0)
        dummy.next=self.head
        temp=dummy
        for _ in range(left-1):
            temp=temp.next
        curr=temp.next
        for _ in range(right-left):
            nxt=curr.next  #3
            curr.next=nxt.next
            nxt.next=temp.next
            temp.next=nxt
        return dummy.next
            
        
                
    def print_list(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("END")
    
            
    
    #time complexity O(n) space O(1)
ll=Linkedlist()
arr=[5,4,3,2,1]
for i in arr:
    ll.insert_at_begining(i)
# ll.insert_at_begining(3)
# ll.insert_at_begining(2)
# ll.insert_at_begining(1)
# ll.insert_at_end(4)
# ll.insert_at_end(5)
# ll.insert_at_end(6)
ll.print_list()
# print(ll.is_cycle())
# ll.reverse_list()
# ll.remove_end(2)
# ll.remove_nth_end(2)
# print(ll.odd_even())
# ll.even_to_even()
# ll.odd_than_even()
# ll.swap_node()
ll.reversenth(2,4)
ll.print_list()

            
        