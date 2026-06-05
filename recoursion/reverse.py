import math
def rev(n):
    dig=int(math.log10(n))+1
    return helper(n,dig)
def helper(n,dig):
    if n%10==n:
        return n
    rem=n%10
    return rem*int(math.pow(10,dig-1))+helper(n//10,dig-1)
def rev2(n,ans):
    if n==0:
        return ans
    rem=n%10
    return rev2(n//10,ans*10+rem)
print(rev(1234))
print(rev2(1234,0))
