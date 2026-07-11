class Node:
    def  __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Browserhistory:
    def  __init__(self):
        self.head=None
        self.current=None
    
    
    def visit(self,data):
        new_node=Node(data)
        if self.current is None:
            self.current=new_node
            self.head=new_node
            return
        if self.current.next is None:
            self.current.next=new_node
            new_node.prev=self.current
            self.current=new_node          
            return
        self.current.next=None
        self.current.next=new_node
        new_node.prev=self.current
        self.current=new_node
        return
    
        
    def backword(self):
        if self.current is None:
            return "list is empty"
        s=self.current.prev
        if s:
            self.current=s
            return s.data
        return "you not visit any url"
    
    def forword(self):
        if self.current is None:
            return "list is empty"
        temp=self.current.next
        if temp:
            self.current=temp
            return temp.data
        return "that last url"
    
    def print_data(self):
        if self.current is None:
            return "list is empty"
        temp=self.head
        while temp:
            print(f"{temp.data}",end=" ")
            temp=temp.next
        print("END")
        
    
ll=Browserhistory()
ll.visit("google")
ll.visit("youtube")
ll.visit("leetcode")
ll.print_data()
print(ll.backword())
print(ll.backword())
print(ll.backword())
ll.print_data()
ll.visit("hotstar")
ll.print_data()
print(ll.backword())
ll.print_data()
print(ll.forword())
ll.print_data()

