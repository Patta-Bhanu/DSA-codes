class Solution:
    def combinationSum(self, candidates, target):
        res=[]
        def combine(idx,curr,total):
            if total==target:
                res.append(curr[:])
                return 
            if target < total or idx==len(candidates):
                return 
            curr.append(candidates[idx])
            combine(idx,curr,total+candidates[idx])
            curr.pop()
            combine(idx+1,curr,total)
        combine(0,[],0)
        return res

obj=Solution()
print(obj.combinationSum([2,3,6,7],7))