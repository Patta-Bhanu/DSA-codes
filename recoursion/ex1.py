def print1(n):
    if n>10:
        return
    print(n," ",end="")
    print1(n+1)
print1(1)