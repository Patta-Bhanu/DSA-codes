class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=[x.lower() for x in s if x.isalnum()]
        l=0
        h=len(lst)-1
        while l<=h:
            if lst[l]!=lst[h]:
                return False
            l+=1
            h-=1
        return True
obj=Solution()
print(obj.isPalindrome("hello! my name is bhanu,iam"))