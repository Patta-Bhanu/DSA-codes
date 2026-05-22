class Stack:
    def __init__(self, n):
        self.stack = [0] * n
        self.size = n
        self.top = -1

    def push(self, val):
        if self.top == self.size - 1:
            print("Stack Overflow")
            return

        self.top += 1
        self.stack[self.top] = val
        print(val, "pushed")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return

        val = self.stack[self.top]
        self.top -= 1
        print(val, "popped")
        return val

    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
            return

        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def display(self):
        if self.top == -1:
            print("Stack is Empty")
            return

        for i in range(self.top, -1, -1):
            print(self.stack[i])


s = Stack(5)

s.push(10)
s.push(20)
s.push(30)

print("Top Element:", s.peek())

s.display()

s.pop()

s.display()

print("Is Empty:", s.is_empty())
print("Is Full:", s.is_full())