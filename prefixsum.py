class Solution:
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums
obj=Solution()
print(obj.runningSum([1,2,3,4]))