class Solution:
    def maxProfit(self, prices) -> int:
        mini=float('inf')
        maxi=0
        for price in prices:
            mini=min(mini,price)
            if price > mini:
                max1=price-mini
                maxi=max(maxi,max1)
        return maxi
obj=Solution()
print(obj.maxProfit([8,0,6,7,3,9]))