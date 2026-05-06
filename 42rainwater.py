class Solution:
    def trap(self, height: List[int]) -> int:
        maxi=0
        max_right=0
        max_left=0
        l=0
        h=len(height)-1
        while l<h:
            if height[l]<height[h]:
                if height[l]>max_left:
                    max_left=height[l]
                else:
                    maxi+=max_left-height[l]
                l+=1
            else:
                if height[h]>max_right:
                    max_right=height[h]
                else:
                    maxi+=max_right-height[h]
                h-=1
        return maxi
        