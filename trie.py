class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
        self.countprefix=0
        self.wordcount=0

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        current=self.root
        
        for i in word:
            if i not in current.children:
                current.children[i]=TrieNode()
            current=current.children[i]
            current.countprefix+=1
        current.isEnd=True
        current.wordcount+=1
    
    def search(self,word):
        current=self.root
        
        for i in word:
            if i not in current.children:
                return False
            current=current.children[i]
        return current.isEnd
    

    
    def delete(self,word):
        self.dlete(self.root,word,0)
    
    def dlete(self,node,word,index):
        if index == len(word):

            if node.wordcount == 0:
                return False, False

            node.wordcount -= 1

            if node.wordcount == 0:
                node.isEnd = False

            return True, (
                node.wordcount == 0
                and len(node.children) == 0
                )
        ch = word[index]

        if ch not in node.children:
            return False, False
        
        deleted, shouldDelete = self.dlete(
            node.children[ch],
            word,
            index + 1
            )
        
        if not deleted:
            return False, False
        
        if deleted:
            node.children[ch].countprefix -= 1
        if shouldDelete:
            del node.children[ch]
        
        return (
            True,
            node.wordcount == 0
            and len(node.children) == 0
            )
        
    
    def display(self):
        self._display(self.root,"")
    
    def _display(self,node,word):
        
        if node.isEnd:
            print(word)
        
        for ch,child in node.children.items():
            self._display(child,word+ch)
         
    def print_tree(self):

        self._print(self.root, "")

    def _print(self, node, indent):

        for ch, child in node.children.items():

            print(indent + ch, f" (True ,{child.wordcount})" if child.isEnd else "")

            self._print(child, indent + "   ")
    

    
    def startwith(self,word):
        current=self.root
        
        for i,j in enumerate(word):
            
            if j not in current.children:
                return 0
            current=current.children[j]
            if current.isEnd:
                return i+1
            
        return 0
    def replace(self,word):
        arr=[]
        for j in word.split():
            k=self.startwith(j)
            if k>=1:
                arr.append(j[:k])
            else:
                arr.append(j)
                
        return " ".join(arr)
    
    def search_new(self,word):
        
        def dfs(node,index):
            
            if index==len(word):
                return node.isEnd
            ch=word[index]
            
            if ch==".":
                
                for i in node.children.values():
                    
                    if dfs(i,index+1):
                        return True
                return False
            
            
            if ch not in node.children:
                return False
            return dfs(node.children[ch],index+1)
        return dfs(self.root,0)

    
    #longest common prefix trie se solwed kiya isko horizontal scanning se bhi solwed kart sakte hai lc 14
    def longestcommon(self):
        curr=self.root
        print(len(curr.children))
        ans=""
        while len(curr.children) ==1 and not curr.isEnd:
            ch=next(iter(curr.children))
            ans+=ch
            curr=curr.children[ch]
        return ans
    
    def count(self,word):
        curr=self.root
        
        for i in word:
            if i not in curr.children:
                return 0
            curr=curr.children[i]
        return curr.countprefix
    
    def wordcountto(self,word):
        curr=self.root
        
        for i in word:
            if i not in curr.children:
                return 0
            curr=curr.children[i]
        return curr.wordcount
    
    
t=Trie()
t.insert("flow")
t.insert("flow")
t.insert("flight")
t.delete("flow")
t.print_tree()
print(t.wordcountto("flow"))
print(t.count("flo"))
print(t.count("flo"))
print(t.wordcountto("flow"))
print(t.longestcommon())
a="this cow carteen"
print(t.replace(a))
t.display()
print(t.search_new("..k"))
print(t.startwith1("car"))