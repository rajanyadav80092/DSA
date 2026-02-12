class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Circularlinkeddoubly:
    def __init__(self):
        self.head=None
        
    def insert_at_bigining(self,data):
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
    def insert_at_between(self,key,data):
        if self.head is None:
            print("list is empty")
            return True
        new_node=Node(data)
        if self.head is None:
            print("list is empty")
        temp=self.head
        while temp.next != self.head:
            if temp.data == key :
                next_node=temp.next
                temp.next=new_node
                new_node.prev=temp
                new_node.next=next_node
                next_node.prev=new_node
                return
            temp=temp.next
        if temp.data==key:
            temp.next=new_node
            new_node.next=self.head
            new_node.prev=temp
            self.head.prev=new_node
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
    def print_forword(self):
        if self.head is None:
            print("list is empty")
            return True
        temp=self.head
        while temp.next != self.head:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data,end=" ")
        return True
    
    def print_backword(self):
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
            if temp == self.head.prev:
                break
    def give_reference(self,data):
        if self.head is None:
            return
        temp=self.head
        while temp.next != self.head:
            if temp.data==data:
                return temp
            temp=temp.next
        if temp.data == data:
            return temp
        return
    
    def delete_reference(self,node):
        #case 1 none is empty
        if self.head is None and node is None:
            print("node not found or node is none")
            return
        
        #case 2 
        if self.head==node and node.next==node:
            self.head=None
            print("only one node and deleted ")
            return 
        
        #case 3 
        if node==self.head:
            last=self.head.prev
            self.head=self.head.next
            self.head.prev=last
            last.next=self.head
            print("head node is remove")
            return 
        
        #case 4 middle and last node delete
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node
        print("middle or last node is deleted")
        return
            
       
    def delete_node(self,data):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        if temp.data is data:
            if temp.next == self.head:
                self.head=None
                print(f"{data} is removed")
                return 
            last=self.head
            while last.next!= self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            print(f"{data} is removed")
            return
        prev=None
        while temp.next != self.head and temp.data != data:
            prev=temp
            temp=temp.next
        if temp.data != data:
            print("data is not found")
            return
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        print(f"{data} is removed")
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
        print(leng)
        return True
    
    
    def circular_list(self):
        if self.head is None:
            print("list is empty")
            return True
        slow=self.head
        fast=self.head
        while True:
            fast=fast.next
            if fast.next is None:
                print("list is not circular")
                return False
            fast=fast.next
            slow=slow.next
            if slow == fast:
                print("list is circular")
                return True
            
    def midiam(self):
        if self.head is None:
            print("list is empty")
            return
        fast=self.head
        slow=self.head
        while fast.next != self.head and fast.next.next != self.head:
            fast=fast.next.next
            slow=slow.next
        print(slow.data)
        return
    
    def swap_around_target(self, target):
        if self.head is None or self.head.next == self.head:
            return "not enough nodes"

        curr = self.head
        while True:
            if curr.data == target:
                left = curr.prev
                right = curr.next

                    # if only 2 nodes
                if left == curr or right == curr:
                    return "not enough nodes"

                left_prev = left.prev
                right_next = right.next

                # left_prev -> right
                left_prev.next = right
                right.prev = left_prev

                # right -> curr
                right.next = curr
                curr.prev = right

                # curr -> left
                curr.next = left
                left.prev = curr

                # left -> right_next
                left.next = right_next
                right_next.prev = left

                # update head if needed
                if left == self.head:
                    self.head = right
                return "swap done"
            curr = curr.next
            if curr == self.head:
                break
        return "target not found"

    
                
            
            
            
cll=Circularlinkeddoubly()
cll.insert_at_bigining(1)
cll.insert_at_bigining(2)
# cll.insert_at_bigining(3)
# cll.insert_at_between(3,4)
cll.print_forword()
print()
print(cll.swap_around_target(2))
cll.print_forword()
                
            
    
        