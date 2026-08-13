class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x= set(nums)
        lcs = 0

        for i in x:
            if i-1 not in x:
                cn = i
                cl = 0
                while cn in x:
                    cn = cn+1
                    cl = cl+1
                lcs = max(cl,lcs)
        return lcs