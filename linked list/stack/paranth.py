class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        mp={"}":"{","]":"[",")":"("}      
        for ch in s:
            if ch in mp:
                if lst and lst[-1]==mp[ch]:
                    lst.pop()
                else:
                    return False
            else:
                lst.append(ch)
        return len(lst)==0 
obj=Solution()
print(obj.isValid("[]"))