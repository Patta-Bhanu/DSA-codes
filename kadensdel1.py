class Solution:
    def maximumSum(self, nums):
        nodel = nums[0]
        onedel = 0
        ans = nums[0]
        for i in range(1, len(nums)):
            prev = nodel
            nodel = max(nodel + nums[i], nums[i])
            onedel = max(onedel + nums[i], prev)
            ans = max(ans, nodel, onedel)
        return ans
obj=Solution()
print(obj.maximumSum([1,-2,0,3]))