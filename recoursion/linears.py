def linears(nums,target,i):
    if i==len(nums):
        return -1
    if nums[i]==target:
        return i
    return linears(nums,target,i+1)
print(linears([1,2,3,45,32,12,49],49,0))