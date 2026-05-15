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
    def maxSubArray2(self, nums):
        summ=nums[0]
        maxi=nums[0]
        for i in range(1,len(nums)):
            summ=max(summ+nums[i],nums[i])
            maxi=max(maxi,summ)
        return maxi
obj=Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(obj.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))