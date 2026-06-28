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
        self.postorder_l(self.root)
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
        return "data not found"
    
   
    
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
        if self.root is None:
            return self.root
        
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
            
    def mindepth(self):
        if self.root is None:
            return 0
        queue=deque([(self.root)])
        depth=0
        while queue:
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth+=1
        return depth
        
            
            
    
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
        if  root is None:
            return 0
        return root.data+self.sum_left(root.left)
    
    def kth(self,k):
        return self.kthlargest(self.root,k)
    
    def kthlargest(self,root,k):
        if root is None:
            return
        stack=[]
        curr=root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.right
            curr=stack.pop()
            k-=1
            if k==0:
                return curr.data
            curr=curr.left
        return None
    
    def valid(self):
        return self.isValidBST(self.root)
    
    def isValidBST(self,root):
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.data < high):
                return False
            return (validate(node.left, low, node.data) and validate(node.right, node.data, high))
        return validate(root, float("-inf"), float("inf"))
    
    def rightview(self):
        return self.rightSideView(self.root)
    def rightSideView(self,root):
        if root is None:
            return []
        res = []

        def dfs(node, level):
            if not node:
                return

        # first time we visit this level
            if level == len(res):
                res.append(node.data)

        # RIGHT first (important)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return res
    
    def leftSide(self):
        if self.root is None:
            return []
        result=[]
        queue=deque([self.root])
        
        while queue:
            
            for i in range(len(queue)):
                node=queue.popleft()
                if i==0:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
    
    
    #question 2 dfs lagega 
    def max_sum(self):
        return self.max_gold(self.root)
    def max_gold(self,root):
        if not root :
            return 0
        left_sum=self.max_gold(root.left)
        right_sum=self.max_gold(root.right)
        return root.data+max(left_sum,right_sum)
    
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
    
    def maxiPath(self):
        return self.maximumPathsum(self.root)
    
    def maximumPathsum(self,root):
        self.ans=float("-inf")
        
        def helper(node):
            if not node:
                return 0
            left=max(0,helper(node.left))
            right=max(0,helper(node.right))
            
            
            current=left+right+node.data
            self.ans=max(current,self.ans)
            
            print(node.data+max(left,right))
            return node.data+max(left,right)
        helper(root)
        
        return self.ans
    
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
        return self.ans
    
    def LCA(self,p,q):
        return self.lca(self.root,p,q)

    
    def lca(self,root,p,q):
        if root is None:
            return None
        temp=root
        while temp:
            if temp.data>p and temp.data>q:
                temp=temp.left
            elif temp.data<p and temp.data<q:
                temp=temp.right
            else:
                return temp.data
        return "lca not found"
    

    
    def maxiwidth(self):
        if self.root is None:
            return "tree is empty"
        queue=deque([self.root])
        pass
    
    def bound(self):
        return self.boundaryTraversal(self.root)
    
    def isLeaf(self, node):
        return node.left is None and node.right is None

    def addLeftBoundary(self, root, ans):
        curr = root.left

        while curr:

            if not self.isLeaf(curr):
                ans.append(curr.data)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def addLeaves(self, root, ans):

        if root is None:
            return

        if self.isLeaf(root):
            ans.append(root.data)
            return

        self.addLeaves(root.left, ans)
        self.addLeaves(root.right, ans)

    def addRightBoundary(self, root, ans):

        curr = root.right
        temp = []

        while curr:

            if not self.isLeaf(curr):
                temp.append(curr.data)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        for i in range(len(temp)-1, -1, -1):
            ans.append(temp[i])

    def boundaryTraversal(self, root):

        if root is None:
            return []

        ans = []

        if not self.isLeaf(root):
            ans.append(root.data)

        self.addLeftBoundary(root, ans)

        self.addLeaves(root, ans)

        self.addRightBoundary(root, ans)

        return ans
        
  
        
            
    
            
            
        
    

    
bst=BSR()
a=[5,2,6]
for i in a:
    bst.insert(i)

print("boundary")
print(bst.bound())
# print("zigzag")
# print(bst.zigzagg())
# print("vertical order")
# print(bst.verticalOrder())
# print("minimum depth")
# print(bst.mindepth())
# print("buttom")
# print(bst.buttomView())
# print("largest binary")
# print(bst.largestBST())
# print("Top view")
# print(bst.topView())
# print("LCA")
# print(bst.LCA(12,18))
# print("balanced")
# print(bst.balance())
# # print(bst.max_sum())
print("maximum path sum")
print(bst.maxiPath())
# # print(bst.rightview())
# print(bst.leftSide())
# print(bst.company())
# print(bst.search_and(10))
# print(bst.kth(3))
# print(bst.sum_node())
# bst.delete(25)
# print(bst.display())
# print(bst.mini())
# print(bst.maxi())
# print(bst.mini())
# bst.maxi()
# bst.count()
# print(bst.search(23))
# # bst.inorder()
# # print("preorder")
# # bst.preorder()
# # print("postorder")
# # bst.postorder()
# print(bst.search(30))
# print("height")
# print(bst.height())
# print(bst.level_order())
# print(bst.valid())
bst.display()