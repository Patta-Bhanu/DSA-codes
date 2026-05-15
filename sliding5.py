class Solution:
    def numSubarrayProductLessThanK(self, nums, k) -> int:
        if k <= 1:
            return 0
        l = 0
        prod = 1
        count = 0
        for r in range(len(nums)):
            prod *= nums[r]
            while prod >= k:
                prod //= nums[l]
                l += 1
            count += (r - l + 1)
        return count
obj=Solution()
print(obj.numSubarrayProductLessThanK([1,23,2,11,4,5],100))