class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(idx, curr):
            if idx == len(nums):
                res.append(curr[:])
                return

            # Take nums[idx]
            curr.append(nums[idx])
            backtrack(idx + 1, curr)

            # Don't take nums[idx]
            curr.pop()
            backtrack(idx + 1, curr)

        backtrack(0, [])
        return res
obj=Solution()
print(obj.subsets([1,2,3]))