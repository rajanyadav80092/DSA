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
    
    def sortList(self):
            self.head=self.merge_sort(self.head)
    def merge_sort(self,head):
        if head is None or head.next is None:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        left=self.merge_sort(head)
        right=self.merge_sort(mid)
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
        if l1 :
            temp.next=l1
        if l2:
            temp.next=l2
        return dummy.next
    
    def insertion(self):
        if self.head is None:
            return "list is empty"
        dummy=Node(0)
        curr=self.head
        while curr:
            prev=dummy
            nxt_node=curr.next
            while prev.next and prev.next.data<curr.data:
                prev=prev.next
            #pointer
            curr.next=prev.next
            prev.next=curr
            curr=nxt_node
        self.head=dummy.next
        return dummy.next
    
    def insertion_sort(self):
        arr=[]
        temp=self.head
        while temp:
            arr.append(temp.data)
            temp=temp.next
        for i in range(1,len(arr)):
            key=arr[i]
            j=i-1
            while j>=0 and key<=arr[j]:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        dummy=Node(0)
        temp=dummy
        for i in arr:
            temp.next=Node(i)
            temp=temp.next
        self.head=dummy.next
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
        # dummy.next=self.head
        return dummy.next
    
    def removelastnth_node(self,n):
        if self.head is None:
            return "list is empty"
        # if n==0:
        #     return self.head
        fast=self.head
        a=[]
        while fast:
            a.append(fast.data)
            fast=fast.next
        m=len(a)
        c=m-n
        dummy=Node(0)
        dummy.next=self.head
        temp=dummy
        for i in range(len(a)):
            if i==c:
                continue
            temp.next=Node(a[i])
            temp=temp.next
        self.head=dummy.next
        return dummy.next
    
    def remove_val(self,val):
        if self.head is None:
            return "link list is empty"
        dummy=Node(0)
        dummy.next=self.head
        slow=dummy
        fast=self.head
        while fast:
            if fast.data==val:
                slow.next=fast.next
                fast=fast.next
            else:
                slow=slow.next
                fast=fast.next
        self.head=dummy.next
        return self.head  
    
    def array_delete(self,nums):
        if self.head is None:
            return "list is empty"
        temp=self.head
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        while temp:
            if temp.data in nums:
                prev.next=temp.next
            else:
                prev=prev.next
            temp=temp.next
        self.head=dummy.next
        return dummy.next  
    
        
    def delete_middle(self):
        if self.head is None:
            return "list is empty"
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        slow=self.head 
        fast=self.head
        while fast and fast.next:
            prev=prev.next
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        # while slow:
        #     slow=slow.next
        return prev.next
    
    def swap_node_start_end_kth(self,k):
        if self.head is None:
            return "list is empty"
        slow=self.head
        fast=self.head
        
        for _ in range(k-1):
            fast=fast.next
        first=fast
        
        while fast.next:
            slow=slow.next
            fast=fast.next
        second=slow
        first.data,second.data=second.data,first.data
        return self.head
                
ll=Linkedlist()
# ll.insert_at_begining(6)
# ll.insert_at_begining(6)
# ll.insert_at_begining(6)
# ll.insert_at_begining(6)
ll.insert_at_begining(2)
ll.insert_at_begining(1)
ll.insert_at_begining(2)
ll.insert_at_begining(3)
ll.insert_at_begining(6)
ll.insert_at_begining(5)
ll.insert_at_begining(28)
ll.print_forward()
ll.reversekth(2,7)
# ll.midial_last()
# ll.remove(6)
ll.insertion()
# print(ll.insertion_sort())
# ll.removelastnth_node(6)
# ll.swap_node_start_end_kth(2)
# ll.delete_middle()
# ll.sortList()

# ll.remove_val(2)
ll.print_forward()

        
        