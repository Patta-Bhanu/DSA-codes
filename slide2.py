class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        maxi = 0
        left = 0
        right = 0
        for st in s:
            while st in se:
                se.remove(s[left])
                left += 1
            se.add(st)
            right += 1
            maxi = max(maxi, right - left)
        return maxi
obj = Solution()
print(obj.lengthOfLongestSubstring("iufdsukjgdsjk"))