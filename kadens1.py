class Solution:
    def maxSubArray(self, nums):
        maxi=float('-inf')
        summ=0
        for i in range(len(nums)):
            summ=0
            for j in range(i,len(nums)):
                summ+=nums[j]
                maxi=max(maxi,summ)
        return maxi
obj=Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))