from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class Binarysearch:
    def __init__(self):
        self.root=None
    
    def insert_data(self,data):
        new_root=Node(data)
        if self.root is None:
            self.root=new_root
            return 
        temp=self.root
        while True:
            if temp.data>data:
                if temp.left is None:
                    temp.left=new_root
                    return
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_root
                    return
                temp=temp.right
    
    def largestKth(self,k):
        if self.root is None:
            return  "tree is empty"
        temp=self.root
        curr=[]
        while curr or temp:
            while temp:
                curr.append(temp)
                temp=temp.right
                
            pop_curr=curr.pop()
            k-=1
            if k==0:
                return pop_curr.data
            temp=pop_curr.left
        return "data is not found"

    def leftView(self):
        if self.root is None:
            return "tree is empty"
        queue=deque([self.root])
        result=[]
        while queue:
            n=len(queue)
            for i in range(n):
                node=queue.popleft()
                if i==0:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
    def rightView(self):
        if self.root is None:
            return "tree is empty"
        queue=deque([self.root])
        result=[]
        while queue:
            n=len(queue)
            for i in range(n):
                node=queue.popleft()
                if i==n-1:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
    def zigzag(self):
        if self.root is None:
            return "tree is empty"
        queue=deque([self.root])
        result=[]
        rev=True
        while queue:
            l=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                l.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if not rev:
                l.reverse()
            result.append(l)
            rev=not rev
        return result
    
    def diameterOfBinaryTree_l(self):
        return self.diameterOfBinaryTree(self.root)
    
    def diameterOfBinaryTree(self, root):

        self.diameter = 0

        def dfs(node):

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.diameter
    
    def inorder(self):
        return self.inorder_l(self.root)
    
    def inorder_l(self,root):
        if root is None:
            return 
        self.inorder_l(root.left) 
        print(root.data) 
        self.inorder_l(root.right)     
            
    def preorder(self):
        return self.preorder_l(self.root)
    
    def preorder_l(self,root):
        if root is None:
            return 
        print(root.data)
        self.preorder_l(root.left)
        self.preorder_l(root.right)
    
    def postorder(self):
        return self.postorder_l(self.root)
    
    def postorder_l(self,root):
        if root is None:
            return
        self.postorder_l(root.left)
        self.postorder_l(root.right)
        print(root.data)
        
    
                
        
    
    

bst=Binarysearch()
a=[10,5,3,7,15,20,12]
for i in a:
    bst.insert_data(i)
# print(bst.largestKth(9))
# print(bst.leftView())
# print(bst.daimeter())
# print(bst.rightView())
# bst.inorder()
print("preorder")
bst.preorder()
print()
print(bst.diameterOfBinaryTree_l())
# print(bst.zigzag())
            