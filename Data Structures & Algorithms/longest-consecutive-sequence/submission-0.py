class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        x = set(nums)
        for i in x:
            if i-1 not in x:
                cs = 0
                cn = i
                while cn in x:
                    cs = cs+1
                    cn = cn+1
                res = max(res,cs)
        return res