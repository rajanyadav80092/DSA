from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class BinaryTree:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
            return 
        temp=deque([self.root])
        while temp:
            q=temp.popleft()
            if q.left is None:
                q.left=new_node
                return 
            else:
                temp.append(q.left)
            if q.right is None:
                q.right= new_node
                return
            else:
                temp.append(q.right)
    
    def inorder(self):
        return self.inorder_l(self.root)
    
    def inorder_l(self,root):
        if root is None:
            return "tree is empty"
        self.inorder_l(root.left)
        print(root.data)
        self.inorder_l(root.right)
    
    def search(self,data):
        if self.root is None:
            return "tree is empty"
        temp=deque([self.root])
        while temp:
            n=len(temp)
            for _ in range(n):
                node=temp.popleft()
                if node.data==data:
                    return "data in binary tree"
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
        return "data not in binary tree"
    
    def diameter(self):
        return self.dia(self.root)
    
    def dia(self,root):
        if root is None:
            return "tree is empty"
        
        def helper(node):
            if not node:
                return (0,0)
            lh,ld=helper(node.left)
            rh,rd=helper(node.right)
        
            height=1+max(lh,rh)
        
            dd=max(
                1+lh+rh,
                ld,
                rd)
            return height,dd
        return helper(root)[0]
    
    def lca(self,p,q):
        return self.lca_node(self.root,p,q)
    
    def lca_node(self,root,p,q):
        if root is None:
            return None
        
        if root.data == p or root.data == q:
            return root.data
        
        left=self.lca_node(root.left,p,q)
        right=self.lca_node(root.right,p,q)
        
        if left and right:
            return root.data
        
        return left if left else right
    
    def levelOrder(self):
        if self.root is None:
            return "tree is empty"
        temp=deque([self.root])
        result=[]
        while temp:
            n=len(temp)
            l=[]
            for _ in range(n):
                node=temp.popleft()
                l.append(node.data)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            result.append(l)
        return result
    
    def maximum(self):
        return self.maxi(self.root)
    
    def maxi(self,root):
        
        self.ans=0
        def helper(node):
            if not node:
                return 0
            left=max(0,helper(node.left))
            right=max(0,helper(node.right))
            
            curr=left+right+node.data
            self.ans=max(curr,self.ans)
            
            return max(left,right)+node.data
        helper(root)
        return self.ans
    
    def left_view(self):
        if self.root is None:
            return "tree is empty"
        temp=deque([self.root])
        result=[]
        while temp:
            n=len(temp)
            
            for i in range(n):
                node=temp.popleft()
                if i==0:
                    result.append(node.data)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
        return result
    
        
    
    def right_view(self):
        if self.root is None:
            return "tree is empty"
        temp=deque([self.root])
        result=[]
        while temp:
            n=len(temp)
            for i in range(n):
                node=temp.popleft()
                if i==n-1:
                    result.append(node.data)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

                
        return result
            
    def topView(self):
        if self.root is None:
            return "Tree is empty"
        queue=deque([(self.root,0)])
        hash={}
        hd=0
        while queue:
            n=len(queue)
            for _ in range(n):
                node,hd=queue.popleft()
                if hd not in hash:
                    hash[hd]=node.data
                if node.left:
                    queue.append((node.left,hd-1))
                if node.right:
                    queue.append((node.right,hd+1))
        arr=[]
        for i in sorted(hash):
            arr.append(hash[i])
        return arr
                
                   
        
        
    
    
bt=BinaryTree()
a=[10,21,5,2,13,15,34]
for i in a:
    bt.insert(i)
bt.inorder()
# print(bt.search(100))
print("top view")
print(bt.topView())
print(bt.diameter())
print("print lca")
print(bt.lca(15,34))
print("levelorder")
print(bt.levelOrder())
print("max_sum")
print(bt.maximum())
print("leftView")
print(bt.left_view())
print("rightView")
print(bt.right_view())
    
            