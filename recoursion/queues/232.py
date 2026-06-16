class MyQueue:

    def __init__(self):
        self.queue = []
        self.front = 0

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        val = self.queue[self.front]
        self.front += 1
        return val

    def peek(self) -> int:
        return self.queue[self.front]

    def empty(self) -> bool:
        return self.front == len(self.queue)
obj = MyQueue()
print(obj.push(1),obj.push(2),
obj.peek(),
obj.pop() ,
obj.empty())
