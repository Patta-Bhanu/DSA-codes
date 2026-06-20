from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = deque()
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.dq) == self.k:
            return False
        self.dq.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.dq) == self.k:
            return False
        self.dq.append(value)
        return True

    def deleteFront(self) -> bool:
        if not self.dq:
            return False
        self.dq.popleft()
        return True

    def deleteLast(self) -> bool:
        if not self.dq:
            return False
        self.dq.pop()
        return True

    def getFront(self) -> int:
        if not self.dq:
            return -1
        return self.dq[0]

    def getRear(self) -> int:
        if not self.dq:
            return -1
        return self.dq[-1]

    def isEmpty(self) -> bool:
        return len(self.dq) == 0

    def isFull(self) -> bool:
        return len(self.dq) == self.k

onj=MyCircularDeque(5)
print(onj.insertFront(10))
print(onj.insertFront(20))
print(onj.insertLast(100))
print(onj.getFront())
print(onj.getRear())