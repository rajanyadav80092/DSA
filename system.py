from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Binarysearch:
    def __init__(self):
        self.root=None
    
    def insert_l(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
            return
        temp=self.root
        while True:
            if temp.data>data:
                if temp.left is None:
                    temp.left=new_node
                    return
                temp=temp.left
            elif temp.data<data:
                if temp.right is None:
                    temp.right=new_node
                    return
                temp=temp.right
            else:
                if temp.data==data:
                    return
    
    def search(self,data):
        if self.root is None:
            return "tree is empty"
        temp=self.root
        while temp:
            if temp.data==data:
                return temp
            if temp.data>data:
                temp=temp.left
            elif temp.data<data:
                temp=temp.right
        return "data is not found"
    
    def inorder(self):
        if self.root is None:
            print("tree is empty")
            return
        return self.inorder_l(self.root)
    def inorder_l(self,root):
        if root is None:
            return
        self.inorder_l(root.left)
        print(root.data)
        self.inorder_l(root.right)
    
    def postorder(self):
        if self.root is None:
            print("tree is empty")
            return
        return self.postorder_l(self.root)
    
    def postorder_l(self,root):
        if root is None:
            return 
        self.postorder_l(root.left)
        self.postorder_l(root.right)
        print(root.data)
    
    def preorder(self):
        if self.root is None:
            print("tree is empty")
            return
        return self.preorder_l(self.root)
    def preorder_l(self,root):
        if root is None:
            return 
        print(root.data)
        self.preorder_l(root.left)
        self.preorder_l(root.right)

    #level order
    def level(self):
        if self.root is None:
            return "tree is empty"
        queue=deque([self.root])
        result=[]
        while queue:
            l=[]
            n=len(queue)
            for _ in range(n):
                node=queue.popleft()
                l.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(l)
        return result
    #isko zigzag karna hota to pahle level ko true than false than true kr ke reverse append krte 
    def sum_all(self):
        if self.root is None:
            print("tree is empty")
            return
        return self.sumNode(self.root)
    def sumNode(self,root):
        if root is None:
            return 0
        left=self.sumNode(root.left)
        right=self.sumNode(root.right)
        return root.data+left+right
    
    def count(self):
        if self.root is None:
            print("tree is empty")
            return
        return self.countNodes(self.root)
    
    def countNodes(self,root):
        if root is None:
            return 0
        left=self.countNodes(root.left)
        right=self.countNodes(root.right)
        return 1+left+right
    
    
    def minimumkth(self,k):
        if self.root is None:
            print("tree is empty")
            return
        a=[]
        curr=self.root
        while curr or a:
            while curr:
                a.append(curr)
                curr=curr.left
                
            curr=a.pop()
            k-=1
            if k==0:
                return curr.data
            curr=curr.right
        print("k is out of heght of left node")
        return
    
    def minimumdepth(self):
        if self.root is None:
            print("tree is empty")
            return 
        return self.minimumdepth_l(self.root)
    
    def minimumdepth_l(self,root):
        if root is None:
            return 0
        depth=1
        queue=deque([root])
        while queue:
            n=len(queue)
            for _ in range(n):
                node=queue.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth+=1
        return depth
    
    def rightside(self):
        if self.root is None:
            print("tree is empty")
            return
        return self.rightSide(self.root)
    
    def rightSide(self,root):
        if root is None:
            return
        result=[]
        queue=deque([root])
        while queue:
            a=len(queue)
            for i in range(a):
                node=queue.popleft()
                if i==a-1:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
    def leftside(self):
        if self.root is None:
            print("Tree is empty")
            return
        return self.leftSide(self.root)
    
    def leftSide(self,root):
        if root is None:
            return
        result=[]
        queue=deque([root])
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
    
    def maxi_height(self):
        if self.root is None:
            print("Tree is empty")
            return
        return self.height(self.root)
    
    def height(self,root):
        if root is None:
            return 0
        left=self.height(root.left)
        right=self.height(root.right)
        return 1+max(left,right)
    
        
    
        
    
            
            
            
bst=Binarysearch()
a=[10,8,9,12,15,3,6]
for i in a:
    bst.insert_l(i)
# bst.postorder()
# print(bst.level())
# bst.inorder()
print(bst.minimumdepth())
# print(bst.maxi_height())
# print(bst.rightside())
# print(bst.leftside())
# print(bst.sum_all())
# print(bst.count())
# print(bst.minimumkth(2))
