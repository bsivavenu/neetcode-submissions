class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        # current_num = 0
        for i in range(len(nums)):
            # left_sum = nums[i]
            right_sum = total_sum-left_sum - nums[i]
            if right_sum == left_sum:
                return i
            left_sum =left_sum + nums[i]

        return -1


