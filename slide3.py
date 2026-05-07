class Solution:
    def minSubArrayLen(self, nums,target) -> int:
        l=0
        total=0
        mini=float('inf')
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                mini=min(mini,r-l+1)
                total-=nums[l]
                l+=1
        return mini if mini!=float('inf') else 0
obj=Solution()
print(obj.minSubArrayLen([1,3,5,4,2,6],9))