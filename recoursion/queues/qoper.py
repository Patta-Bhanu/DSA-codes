class myqueue:
    def __init__(self,n):
        self.queue=[0]*n
        self.front=-1
        self.rear=-1
        self.size=n-1
    def enqueue(self,val):
        if self.rear>=self.size:
            print("overflow")
            return
        if self.rear==-1 and self.front==-1:
            self.front+=1
        self.rear+=1
        self.queue[self.rear]=val
        print(val,'enqueued----')
    def dequeue(self):
        if self.front>self.rear:
            print("underflow")
            return
        print(self.queue[self.front],"dequeued---")
        self.front+=1
    def peek(self):
        return self.queue[self.front] if self.front<=self.rear else -1
    def display(self):
        if (self.front == -1 and self.rear==-1) or (self.front>self.rear):
            return "empty"
        temp=self.front
        while temp<=self.rear:
            print(self.queue[temp])
            temp+=1
    def isempty(self):
        return (self.front == -1 and self.rear==-1) or (self.front>self.rear)
    def isfull(self):
        return self.rear>=self.size
obj=myqueue(6)
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.dequeue()
obj.display()
print(obj.isempty())
print(obj.isfull())
print(obj.peek())
print("art by ---starboy")