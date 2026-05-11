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
        result=[]
        while queue:
            level=[]
            n=len(queue)
            for _ in range(n):
                node = queue.popleft() # Step 2: Queue se nikaalo (First person in line)
                level.append(node.data)   # Step 3: Print karo
        
                # Step 4: Uske bacho ko queue ke peeche laga do
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
    
    def mindepth(self):
        if self.root is None:
            return 0
        queue=deque([(self.root)])
        depth=0
        while queue:
            for _ in range(len(queue)):
                node=queue.popleft()
            
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
        b=root.data
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
    
    
          
    #1
    def company(self):
        if self.root is None:
            return []
        queue=deque([self.root])
        result=[]
        while queue:
            n=len(queue)
            l=[]
            for _ in range(n):
                node=queue.popleft()
                l.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(l)
        return result
    #isme maine bfs lagya hai kyuki isme level wise answer chhahiye 
    #time complexity O(n) and space complexity O(w)
    
    #question 2 dfs lagega 
    def max_sum(self):
        return self.max_gold(self.root)
    def max_gold(self,root):
        if root is None:
            return 0
        left_sum=self.max_gold(root.left)
        right_sum=self.max_gold(root.right)
        return root.data+min(left_sum,right_sum)
    
    
    
    def search_and(self,data):
        return self.search_and_ret(self.root,data)
    
    def search_and_ret(self,root,data):
        if not root:
            return
        a=[]
        node=root
        while node:
            if node.data==data:
                a.append(data)
                if node.left:
                    node=node.left
                    a.append(node.data)
                if node.right:
                    node=node.right
                    a.append(node.data)
                return a
            elif node.data<data:
                node=node.right
            elif node.data>data:
                node=node.left
        return 
   
    
bsr=BSR()
bsr.insert(10)
bsr.insert(5)
bsr.insert(6)
bsr.insert(18)
bsr.insert(20)
bsr.insert(15)
bsr.insert(25)
bsr.insert(4)
bsr.insert(23)
bsr.insert(30)
print(bsr.max_sum())
# print(bsr.rightview())
print(bsr.leftSide())
# print(bsr.company())
# print(bsr.search_and(10))
# print(bsr.kth(3))
print(bsr.sum_node())
# bsr.delete(25)
# print(bsr.display())
# print(bsr.mini())
# print(bsr.maxi())
# print(bsr.mini())
# bsr.maxi()
# bsr.count()
# print(bsr.search(23))
# bsr.inorder()
# print("preorder")
# bsr.preorder()
# print("postorder")
# bsr.postorder()
# print(bsr.height())
# print(bsr.mindepth())
# print(bsr.level_order())
# print(bsr.valid())