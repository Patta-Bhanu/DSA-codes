class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        if not self.stack:
            span = self.idx + 1
        else:
            span = self.idx - self.stack[-1][1]

        self.stack.append((price, self.idx))
        return span


# Driver Code
spanner = StockSpanner()

prices = [100, 80, 60, 70, 60, 75, 85]

for price in prices:
    print(f"Price: {price}, Span: {spanner.next(price)}")