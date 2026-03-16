class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Circularlinkedlist:
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
        while temp.next !=self.head:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        return
    
    def insert_at_between(self,target_data,new_data):
        new_node=Node(new_data)
        if self.head is None:
            return "list is empty"
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
            temp.next=new_node
            new_node.prev=temp
            self.head.prev=new_node
            new_node.next=self.head
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
        new_node.next=self.head
        new_node.prev=temp
        new_node.next=self.head
        return
    
    def print_forword(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while True:
            print(temp.data,end=" ")
            temp=temp.next
            if temp == self.head:
                break
        print("END")
    
    def print_backward(self):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        temp=self.head.prev
        while True:
            print(temp.data,end=" ")
            temp=temp.prev
            if temp==self.head.prev:
                break
        print("END")
    
    def midium_node(self):
        if self.head is None:
            return "list is empty"
        fast=self.head
        slow=self.head
        while fast.next != self.head and fast.next.next!= self.head:
            fast=fast.next.next
            slow=slow.next
        return slow.data
        
    def length_list(self):
        if self.head is None:
            return "empty list"
        leng=1
        temp=self.head
        while temp.next != self.head:
            leng+=1
            temp=temp.next
        return leng
            
    def delete_node(self,data):
        if self.head is None:
            return "list is empty"
        temp=self.head
        if temp.data==data:
            if temp.next==temp:
                self.head=None
                return f"{data} is remove"
            last=self.head
            while last.next != self.head:
                last=last.next
            last.next=temp.next
            temp.next.prev=last
            self.head=temp.next
            temp=None
            return f"{data} is remove"
        temp=self.head 
        prev=None
        while temp.next != self.head and temp.data != data:
            prev=temp
            temp=temp.next
        if temp.data != data:
            return "data not found"
        prev.next=temp.next
        temp.next.prev=prev
        temp=None
        return f"{data} is deleted"
    
    def give_reference(self,data):
        if self.head is None:
            return "list is empty"
        temp=self.head
        while temp.next != self.head:
            if temp.data == data:
                return temp
            temp=temp.next
        if temp.data == data:
            return temp
        return None

    def delete_reference(self,node):
        #case 1
        if self.head is None or node is None:
            return "list is empty"
        
        #case 2
        if node.next is node:
            self.head=None
            return "only one node those delete"
        
        #case 3
        if self.head is node and node.next != node:
            prev=node.prev
            nxt=node.next
            prev.next=nxt
            nxt.prev=prev
            self.head=nxt
            return "head node is remove"
        #case 4
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node
        return "middlee or last node remove"
    
    
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
    
cll=Circularlinkedlist()
cll.insert_at_begining(1)
cll.insert_at_between(1,2)
cll.insert_at_end(3)
cll.insert_at_begining(4)
n=cll.give_reference(4)
print(cll.delete_reference(n))
# print(cll.delete_node(3))
cll.print_forword()
cll.print_backward()
print(cll.midium_node())
print(cll.length_list())
    
            
            