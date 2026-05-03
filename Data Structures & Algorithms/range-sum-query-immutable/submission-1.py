class NumArray:

    def __init__(self, nums: list[int]):
        # We create a prefix sum array where each index 'i' 
        # stores the sum of all elements before it.
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # The sum from left to right is:
        # (Sum from 0 to right) - (Sum from 0 to left-1)
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)