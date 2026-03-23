# class Queue:
#     def __init__(self):
#         self.stack1=[]
#         self.stack2=[]
        
#     def enqueue(self,item):
#         self.stack1.append(item)
        
#     def dequeue(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         if not self.stack2:
#             return "stack is empty"
#         return self.stack2.pop()
    
#     def front(self):
#         return self.stack1[0]
#     def rear(self):
#         return self.stack1[-1]
    
#     def is_empty(self):
#         return len(self.stack1) == 0
#     def size(self):
#         return len(self.stack1)
# q=Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# print(q.front())
# print(q.rear())
# print(q.size())
# print(q.is_empty())
# print(q.dequeue())


# class Stack:
#     def __init__(self):
#         self.stack=[]
        
#     def push(self,item):
#         self.stack.append(item)
        
#     def pop(self):
#         return self.stack.pop()
        
#     def size(self):
#         return len(self.stack)
    
#     def is_empty(self):
#         return len(self.stack)==0
    
#     def front(self):
#         return self.stack[0]
#     def rear(self):
#         return self.stack[-1]
# s=Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# print(s.front())
# print(s.size())
# print(s.rear())