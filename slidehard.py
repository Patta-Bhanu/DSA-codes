from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_count=Counter(t)
        need=len(t_count)        
        have=0
        l=0
        window={}
        res=[-1,-1]
        res_len=float('inf')
        for r in range(len(s)):
            ch=s[r]
            window[s[r]]=window.get(s[r],0)+1
            if ch in t_count and window[ch]==t_count[ch]:
                have+=1
            while have==need:
                if (r-l+1)<res_len:
                    res=[l,r]
                    res_len=r-l+1
                window[s[l]]-=1
                if s[l] in t_count and window[s[l]]<t_count[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if res_len != float('inf') else ""
obj=Solution()
print(obj.minWindow("anvbceb","abc"))