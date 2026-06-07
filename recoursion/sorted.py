def sorted(nums,i):
    if i==len(nums)-1:
        return True
    if nums[i]>nums[i+1]:
        return False
    return sorted(nums,i+1)
print(sorted([1,2,7,2,90,111,132],0))