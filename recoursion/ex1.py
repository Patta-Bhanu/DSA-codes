def print1(n):
    if n>100:
        return
    print(n)
    print1(n+1)
print1(1)