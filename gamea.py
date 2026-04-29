class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class BSR:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
            return
        temp=self.root
        while True:
            if temp.data==data:
                return
            elif temp.data<data:
                if temp.right is None:
                    temp.right=new_node
                    return
                temp=temp.right
            else:
                if temp.left is None:
                    temp.left=new_node
                    return
                temp=temp.left
    
    def inorder(self):
        if self.root is None:
            print("BSR is empty")
            return
        return self.inorder_l(self.root)
    def inorder_l(self,root):
        if root is None:
            return
        self.inorder_l(root.left)
        print(root.data)
        self.inorder_l(root.right)
    
    def preorder(self):
        if self.root is None:
            print("BSR is empty")
            return
            
        return self.preorder_l(self.root)
    def preorder_l(self,root):
            
        print(root.data)
        self.preorder_l(root.left)
        self.preorder_l(root.right)
    
    def postorder(self):
        return self.postorder_l(self.root)
    
    def postorder_l(self,root):
        if root is None:
            print("BSR is empty")
            return
        self.postorder_l(root.left)
        self.postorder_l(root.right)
        print(root.data)
    
    def mini(self):
        return self.minimum(self.root)
    
    def minimum(self,root):
        if root is None:
            print("bsr is empty")
            return
        curr=root
        while curr.left is not None:
            curr=curr.left
        return curr.data
    
    def maxi(self):
        return self.maximum(self.root)
    
    def maximum(self,root):
        if root is None:
            print("bsr is empty")
        curr=root
        while curr.right is not None:
            curr=curr.right
        return curr
    
    def sum(self):
        return self.sum_nodes(self.root)
    def sum_nodes(self,root):
        if root is None:
            return 0
        return root.data+self.sum_nodes(root.left)+self.sum_nodes(root.right)
    
    def count(self):
        return self.count_nodes(self.root)
    
    def count_nodes(self,root):
        if root is None:
            return 0
        return 1+self.count_nodes(root.left)+self.count_nodes(root.right)
    
    def height(self):
        return self.height_node(self.root)
    def height_node(self,root):
        if root is None:
            return 0
        left=self.height_node(root.left)
        right=self.height_node(root.right)
        return 1+max(left,right)
    
   
    
    def search(self,data):
        if self.root is None:
            return None
        temp=self.root
        while temp:
            if temp.data==data:
                return data
            elif temp.data<data:
                temp=temp.right
            else:
                temp=temp.left
        return -1
   
            
                
bsr=BSR()
a=[10,5,8,15,20,25,40,45]
for i in a:
    bsr.insert(i)
# bsr.maxi()
# bsr.mini()
# bsr.sum()
# bsr.count()
# bsr.height()
bsr.search(45)
print(bsr.delete(20))
bsr.inorder()

        