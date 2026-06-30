class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class circularlinked:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.prev=new_node
            new_node.next=new_node
            return 
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
        new_node.prev=temp
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
                nxt=temp.next
                temp.next=new_node
                new_node.prev=temp
                new_node.next=nxt
                nxt.prev=new_node
                return 
            temp=temp.next
        if temp.data==target_data:
            nxt=temp.next
            temp.next=new_node
            new_node.prev=temp
            new_node.next=nxt
            nxt.prev=new_node
            return 
        print("target data not in linked list")
        
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
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
            return "list is empty"
        temp=self.head
        while temp.next != self.head:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data,end=" ")

cll=circularlinked()
cll.insert_at_begining(1)
cll.insert_at_begining(2)
cll.insert_at_end(3)
cll.insert_at_between(1,4)
cll.print_forword()
        