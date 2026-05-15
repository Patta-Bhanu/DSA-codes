class Solution:
    def searchRange(self, nums, target):
        def first():
            l=0
            h=len(nums)-1
            ans=-1
            while l<=h:
                m=(l+h)//2
                if nums[m]==target:
                    ans=m
                    h=m-1
                elif nums[m]<target:
                    l=m+1
                else:
                    h=m-1
            return ans
        def last():
            l=0
            h=len(nums)-1
            ans=-1
            while l<=h:
                m=(l+h)//2
                if nums[m]==target:
                    ans=m
                    l=m+1
                elif nums[m]<target:
                    l=m+1
                else:
                    h=m-1
            return ans
        return [first(),last()]
obj=Solution()
print(obj.searchRange([11,22,33,44,44,56,78,90],44))