def print1(n):
    if n==0:
        return
    print(n)
    print1(n-1)
    print(n)
print1(5)