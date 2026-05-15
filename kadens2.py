class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        n = len(nums)
        maxi = float('-inf')
        for i in range(n):
            summ = 0
            for j in range(n):
                idx = (i + j) % n
                summ += nums[idx]
                maxi = max(maxi, summ)
        return maxi
    def maxSubarraySumCircular2(self, nums) -> int:
        total=sum(nums)
        mini=nums[0]
        summ=nums[0]
        for i in range(1,len(nums)):
            summ=min(summ+nums[i],nums[i])
            mini=min(summ,mini)
        summ=nums[0]
        maxi=nums[0]
        for i in range(1,len(nums)):
            summ=max(summ+nums[i],nums[i])
            maxi=max(summ,maxi)
        if maxi<0:
            return maxi
        return max(total-mini,maxi)
obj=Solution()
print(obj.maxSubarraySumCircular([1,-2,3,-2]))
print(obj.maxSubarraySumCircular2([1,-2,3,-2]))
