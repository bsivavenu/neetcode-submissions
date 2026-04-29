class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len = 1
        inc = 1 
        dec = 1 

        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                
                inc += 1
                dec = 1 

            elif nums[i+1] < nums[i]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            max_len = max(max_len, inc, dec)

        return max_len