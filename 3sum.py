class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            h=n-1
            while l<h:
                summ=nums[i]+nums[l]+nums[h]
                if 0==summ:
                    res.append([nums[i],nums[l],nums[h]])
                    l+=1
                    h-=1
                    while l < h and nums[l] == nums[l - 1]:
                        l += 1
                    while l < h and nums[h] == nums[h + 1]:
                        h -= 1
                elif 0>summ:
                    l+=1
                else:
                    h-=1
        return res
obj=Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))