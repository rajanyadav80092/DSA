class Queue:
    def __init__(self):
        self.queue=[]
        self.queue2=[]
    
    def push(self,data):
        self.queue.append(data)
        return data
    def pop(self):
        if not self.queue2:
            while self.queue:
                self.queue2.append(self.queue.pop())
        if not self.queue2:
            return "empty queue"
        return self.queue2.pop()
    def get(self):
        if self.queue2:
            return self.queue2
        return self.queue
    
    def length(self):
        if not self.queue:
            return len(self.queue2)
        return len(self.queue)
q=Queue()
q.push(1)
q.push(2)
q.push(3)
q.pop()
print(q.get())
print(q.length())
            
 

                