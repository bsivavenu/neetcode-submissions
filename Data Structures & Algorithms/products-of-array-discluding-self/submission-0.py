class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix,postfix = 1,1
        a = []
        b = []
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix*nums[i]
            a.append(prefix)
        
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*postfix
            postfix = postfix*nums[i]
            b.append(postfix)
            # i -= 1
        print(a)
        print(b)
        return res