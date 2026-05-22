class MinStack:

    def __init__(self):
        self.stack=[]
        self.minst=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minst or val<=self.minst[-1]:
            self.minst.append(val)
    def pop(self) -> None:
        if self.minst[-1]==self.stack[-1]:
            self.minst.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minst[-1]
#Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)