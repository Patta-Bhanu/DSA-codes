class Solution:
    def maxArea(self, height):
        l=0
        h=len(height)-1
        max1=0
        while l<h:
            mini,maxi=height[l],height[h]
            if (min(mini,maxi)*(h-l))>max1:
                max1=min(mini,maxi)*(h-l)
            if mini==min(mini,maxi):
                l+=1
            else:
                h-=1
        return max1

obj=Solution()
print(obj.maxArea([10,9,3,1,43,2,1]))