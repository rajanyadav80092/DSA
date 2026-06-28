from collections import deque
class Root:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        new_root=Root(data)
        if self.root is None:
            self.root=new_root
            return
        q=deque([self.root])
        while q:
            temp=q.popleft()
            if temp.left is None:
                temp.left=new_root
                return
            else:
                q.append(temp.left)
            if temp.right is None:
                temp.right=new_root
                return
            else:
                q.append(temp.right)
        
             
    
    def inorder(self):
        return self.inorder_l(self.root)
        
    def inorder_l(self,root):
        if not root:
            return "tree is empty"
        self.inorder_l(root.left)
        print(root.data)
        self.inorder_l(root.right)
    
    def preorder(self):
        return self.preorder_l(self.root)
    
    def preorder_l(self,root):
        if not root:
            return "tree is empty"
        print(root.data)
        self.preorder_l(root.left)
        self.preorder_l(root.right)
        
    
    def postorder(self):
        return self.postorder_l(self.root)
    
    def postorder_l(self,root):
        if not root:
            return "tree is empty"
        self.postorder_l(root.left)
        self.postorder_l(root.right)
        print(root.data)
        
    
   
    
        
    def tree_right(self):
        return self.tree_right_sum(self.root)
    
    def tree_right_sum(self,root):
        if not root:
            return 0
        return root.data  + self.tree_right_sum(root.right)
    
    def tree_left(self):
        return self.tree_left_sum(self.root)
    
    def tree_left_sum(self,root):
        if not root:
            return 0
        return root.data+self.tree_left_sum(root.left)
    
    def diameter(self):
        return self.diameter_node(self.root)
    
    def diameter_node(self,root):
        if not root:
            return "tree is empty"
        
        def helper(node):
            if not node:
                return (0,0)
            
            lh,ld=helper(node.left)
            rh,rd=helper(node.right)
            
            height=1+max(lh,rh)
            
            dia=max(lh+rh+1,ld,rd)
            
            return height,dia
        return helper(root)[1]

    
    def max_value(self):
        return self.max_values(self.root)
    
    def max_values(self,root):
        if not root:
            return float("-inf")
        left=self.max_values(root.left)
        right=self.max_values(root.right)
        return max(root.data,left,right)
    
    def height(self):
        return self.height_tree(self.root)
    
    
    def height_tree(self,root):
        if not root:
            return 0
        return 1+max(self.height_tree(root.left),self.height_tree(root.right))
    
    def count(self):
        return self.count_node(self.root)
    
    def count_node(self,root):
        if not root:
            return 0
        return 1+self.count_node(root.left)+self.count_node(root.right)
    
    
    def balance(self):
        return self.is_balanced(self.root)
    
    def is_balanced(self,root):
        if not root:
            return "tree is empty"
        def helper(node):
            if not node:
                return (0,True)
            lh,left_balanced=helper(node.left)
            rh,right_balanced=helper(node.right)
            
            height=1+max(lh,rh)
            balanced=left_balanced and right_balanced and abs(lh-rh)<=1
            
            return (height,balanced)
        return helper(root)[1]
    
    def largestBST(self):
        return self.largestBinary(self.root)
    
    def largestBinary(self,root):
        if not root:
            return 0
        
        self.ans = 0
        def helper(node):
            if not node:
                return (True,0,float("inf"),float("-inf"))
            leftBST, leftSize, leftMin, leftMax = helper(node.left)
            rightBST, rightSize, rightMin, rightMax = helper(node.right)
        
            
            size=1+leftSize+rightSize
            if (
                leftBST and
                rightBST and
                leftMax < node.data < rightMin
                ):
                isBST = True
                minVal = min(leftMin, node.data)
                maxVal = max(rightMax, node.data)
                self.ans = max(self.ans, size)
                return (
                    isBST,
                    size,
                    minVal,
                    maxVal
                    )
            return (
                False,
                size,
                float("-inf"),
                float("inf")
                )
                
        helper(root)
        return self.ans,helper(root)[0]
    
    
    def lca(self,p,q):
        return self.lca_node(self.root,p,q)
    def lca_node(self,root,p,q):
        if root is None:
            return None
        if root.data == p or root.data==q:
            return root.data
        left=self.lca_node(root.left,p,q)
        right=self.lca_node(root.right,p,q)
        
        if left and right:
            return root
        return left if left else right
    
    
    def maximum(self):
        return self.maxi(self.root)
    
    def maxi(self,root):
        # if self.root is None:
        #     return None
        self.ans=0
        def helper(node):
            if not node:
                return 0
            left=max(0,helper(node.left))
            right=max(0,helper(node.right))
            
            curr=left+right+node.data
            self.ans=max(curr,self.ans)
            
            return node.data+max(left,right)
        helper(root)
        return self.ans
    
    
    def vertical(self):
        if self.root is None:
            return "tree is empty"
        queue=deque([(self.root,0,0)])
        rows=0
        cols=0
        hash={}
        while queue:
            n=len(queue)
            for _ in range(n):
                node,cols,rows=queue.popleft()
                if cols in hash:
                    hash[cols].append((rows,node.data))
                else:
                    hash[cols]=[]
                    hash[cols].append((rows,node.data))  
                if node.left:
                    queue.append((node.left,cols-1,rows+1))
                if node.right:
                    queue.append((node.right,cols+1,rows+1))
        arr=[]
        
        for cols in sorted(hash):
            hash[cols].sort()
            arr1=[]
            for i,num in hash[cols]:
                arr1.append((i,num))
            arr.append(arr1)
        return arr
    def search(self,data):
        if self.root is None:
            return "tree is empty"
        queue=deque([self.root])
        while queue:
            node=queue.popleft()
            if node.data==data:
                return data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return "data not found"     
    
    def deselizer(self,data):
        if not data:
            return None
        vals=data.split(",")
        root=Root(int(vals[0]))
        q=deque([root])
        i=1
        while q and i<len(vals):
            node=q.popleft()
            if i<len(vals) and vals[i]!="N":
                node.left=Root(int(vals[i]))
                q.append(node.left)
            i+=1
            
            if i<len(vals) and vals[i] != "N":
                node.right=Root(int(vals[i]))
                q.append(node.right)
            i+=1
        return root
                    
        
                
                    

        
bt=BinaryTree()
a="3,N,4,5,N,N,N,6,7,8"
# for i in a:
#     bt.insert(i)
bt.deselizer(a)
# print("vertical order")
# print(bt.vertical())
print("search")
print(bt.search(4))
print("inorder")
bt.inorder()
# print("LCA")
# print(bt.lca(2,22))
# print("postorder")
# print("maximum")
# print(bt.maximum())
# bt.postorder()
# print("preorrder")
# bt.preorder()
# print(bt.levelorder())
# print("zigzag")
# print(bt.zigzag())
# print("diameter")
# print(bt.diameter())
# print(bt.tree_left())
# print("right sum")
# print(bt.tree_right())
# print(bt.count())
# print("max value")
# print(bt.max_value())
# print("count node")
# print(bt.count())
# print("maximum height")
# print(bt.height())
# print("balanced")
# print(bt.balance())
# print("largest")
# print(bt.largestBST())
