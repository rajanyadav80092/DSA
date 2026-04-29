class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=None
        self.right=None
    
class Binary:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
            return
        
            
    
    # def insert(self,data):
    #     new_node=Node(data)
    #     if self.root is None:
    #         self.root=new_node
    #         self.root.left=None
    #         self.root.right=None
    #         return
    # def insert_left(self,data):
    #     new_node=Node(data)
    #     if self.root.left is None:
    #         self.root.left=new_node
    #         return
    #     temp=self.root
    #     while temp.left:
    #         temp=temp.left
    #     temp.left=new_node
    #     new_node.left=None
    #     new_node.right=None
    #     return
    # def insert_right(self,data):
    #     new_node=Node(data)
    #     if self.root.right is None:
    #         self.root.right=new_node
    #     temp=self.root.right
    #     while temp.right:
    #         temp=temp.right
    #     temp.right=new_node
    #     new_node.right=None
    #     new_node.left=None
    #     return

b=Binary()
b.insert(3)
b.insert_left(4)
b.insert_left(6)
b.insert_right(5)
