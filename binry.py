class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
    
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
        return
    
    def insert_at_between(self,target_data,new_data):
        new_node=Node(new_data)
        if self.head is None:
            return "list is empty not any target value"
        temp=self.head
        while temp.next:
            if temp.data==target_data:
                nxt=temp.next
                temp.next=new_node
                new_node.prev=temp
                new_node.next=nxt
                nxt.prev=new_node
                return
            temp=temp.next
        if temp.data==target_data:
            temp.next=new_node
            new_node.prev=temp
            return
        return "target not found"
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        return
    
    def print_forword(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while temp:
            prev_data = temp.prev.data if temp.prev else None

            print(prev_data, temp.data)
            # print(f"{temp.prev} : {temp.data}" ,end=" ")
            temp=temp.next
        print("END")
        
    def give_Reference(self,data):
        if self.head is None:
            return None
        temp=self.head
        while temp.next:
            if temp.data==data:
                return temp
            temp=temp.next
        if temp.data==data:
            return temp
        return None
    
    def delete_reference(self,node):
        #case 1
        if self.head is None or node is None:
            return "list is empty or data incorrect"
        
        #case 2
        if self.head is node and node.next is None:
            self.head=None
            return "only one node those are delete"
        
        #case 3
        if self.head is node:
            self.head=node.next
            node.next.prev=None
            return "head node is  delete"
         
        if node.next is None:
            prev=node.prev
            prev.next=None
            return "last node is deleteed"
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        return "middle node is deleted"
    
    def delete_node(self,data):
        if self.head is None:
            return "list is empty"
        temp=self.head
        if temp.data==data:
            if temp.next is None:
                self.head=None
                return "only one node those are delete"
            self.head=temp.next
            temp.next.prev=None
            temp=None
            return "head node delete"
        
        prev=None
        temp=self.head
        while temp.next and temp.data != data:
            prev=temp
            temp=temp.next
        if temp.data != data:
            return "data not found"
        if temp.data==data and temp.next is None:
            prev=temp.prev
            prev.next=None
            return "last node delete"
        prev=temp.prev
        nxt=temp.next
        prev.next=nxt
        nxt.prev=prev
        return "middle node delete"
    
    def reverse(self):
        if self.head is None:
            return "list is empty"
        temp=None
        curr=self.head
        while curr:
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        if temp:
            self.head=temp.prev
            
            
            
        
    def deleteEndnth(self,n):
        if self.head is None:
            return "list is empty"
        
        dummy=Node(0)
        dummy.next=self.head
        fast=dummy
        for _ in range(n):
            fast=fast.next
            
            if fast is None:
                return "n is greater than linked list"
        slow=dummy
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        
        to_delete=slow.next
        slow.next=to_delete.next
        
        if to_delete.next:
            to_delete.next.prev=slow
            
        if dummy.next:
            dummy.next.prev=None
        self.head=dummy.next
        return
        
        
            
    
dll=Doublylinkedlist()
dll.insert_at_begining(10)
dll.insert_at_between(10,20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.insert_at_end(50)
dll.reverse()
# print(dll.delete_node(30))
# n=dll.give_Reference(20)
# print(dll.delete_reference(n))

# print(dll.deleteEndnth(3))
dll.print_forword()
            