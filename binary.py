from collections import deque
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
            if temp.data<data:
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
        if not self.root  :
            print("BSR is empty")
            return 
        self.inorder_l(self.root)
        
    def inorder_l(self,root):
        if root is None :
            return 
        self.inorder_l(root.left)
        print(root.data)
        self.inorder_l(root.right)
    
    def preorder(self):
        if not self.root:
            return
        self.preorder_l(self.root)
    def preorder_l(self,root):  #Root-L-Right
        if root is None:
            print("bsr is empty")
            return 
        print(root.data)
        self.preorder_l(root.left)
        self.preorder_l(root.right)
    
    def postorder(self):
        if not self.root:
            print("empty bsr")
            return
        self.preorder_l(self.root)
    def postorder_l(self,root):
        if root is None:
            return 
        self.postorder_l(root.left)
        self.postorder_l(root.right)
        print(root.data)
    
    
    def search(self,data):
        if self.root is None:
            return "bsr is empty"
        temp=self.root
        while temp:
            if temp.data==data:
                return data
            elif temp.data>data:
                temp=temp.left
            else:
                temp=temp.right
        return None
    
    def count(self):
        return self.count_nodes(self.root)
    
    def count_nodes(self,root):
        if root is None:
            return 0
        return 1+self.count_nodes(root.left)+self.count_nodes(root.right)
    
    def mini(self):
        return self.minimum_value(self.root)
    
    def minimum_value(self,root):
        if root is None:
            return None
        curr=root
        while curr.left is not None:
            curr=curr.left
        return curr
    
    def maxi(self):
        return self.maximu(self.root)
    def maximu(self,root):
        if root is None:
            return None
        curr=root
        while curr.right is not None:
            curr=curr.right
        return curr
    
    def delete(self,data):
        self.root=self.rdelete(self.root,data)
    
    def rdelete(self,root,data):
        if root is None:
            return None
        if data<root.data:
            root.left=self.rdelete(root.left,data)
        elif data>root.data:
            root.right=self.rdelete(root.right,data)
        elif root.data==data:
            #not child
            if root.left is None and root.right is None:
                return None
            #one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            
            #case 3 two child
            successor = self.maximu(root.right)
            root.data = successor.data
            root.right = self.rdelete(root.right, successor.data)
        return root
    
    def display(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data))
            if node.left or node.right:
                if node.left:
                    self.display(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.display(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")
    
    def level_order(self):
        if not self.root:
            return
    
        queue = deque([self.root]) # Step 1: Root ko queue mein dalo
    
        while queue:
            node = queue.popleft() # Step 2: Queue se nikaalo (First person in line)
            print(node.data, end=" ") # Step 3: Print karo
        
        # Step 4: Uske bacho ko queue ke peeche laga do
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    def height(self):
        return self._height(self.root)
    
    def _height(self,node):
        if not node:
            return 0
        left=self._height(node.left)
        right=self._height(node.right)
        
        return  1+max(left,right)
    
    def sum_node(self):
        return self.sum_left(self.root)
    def sum_left(self,root):
        if not root:
            return 0
        return root.data+self.sum_left(root.right)+self.sum_left(root.left)
        
 
bsr=BSR()
bsr.insert(10)
bsr.insert(5)
bsr.insert(18)
bsr.insert(20)
bsr.insert(15)
bsr.insert(25)
bsr.insert(4)
bsr.insert(23)
bsr.insert(30)
# print(bsr.sum_node())
bsr.delete(25)
print(bsr.display())
# print(bsr.mini())
# print(bsr.maxi())
# print(bsr.mini())
# bsr.maxi()
# bsr.count()
# print(bsr.search(23))
bsr.inorder()
# print("preorder")
# bsr.preorder()
# print("postorder")
# bsr.postorder()
# print(bsr.height())
# bsr.level_order()