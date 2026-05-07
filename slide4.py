from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        p_count=Counter(p)
        window=Counter()
        k=len(p)
        res=[]
        for i in range(len(s)):
            window[s[i]]+=1
            if i>=k:
                if window[s[i-k]]==1:
                    del window[s[i-k]]
                else:
                    window[s[i-k]]-=1
            if p_count==window:
                res.append(i-k+1)
        return res       
obj=Solution()
print(obj.findAnagrams("abanbvcgba","ab"))