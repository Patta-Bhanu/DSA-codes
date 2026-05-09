class Solution:
    def productExceptSelf(self, nums):
        l=1
        n=len(nums)
        res=[1]*n
        for i in range(n):
            res[i]=l
            l*=nums[i]
        r=1
        for j in range(n-1,-1,-1):
            res[j]*=r
            r*=nums[j]
        return res        
obj=Solution()
print(obj.productExceptSelf([2,23,45]))