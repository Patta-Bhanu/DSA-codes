from math import ceil
class Solution:
    def minEatingSpeed(self, piles, h: int):
        def funct(speed):
            total = 0
            for bananas in piles:
                total += ceil(bananas / speed)
            return total
        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            totalh = funct(mid)
            if totalh <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
obj=Solution()
print(obj.minEatingSpeed([2,3,7,8,13],8))