class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

        # x = set()
        # for i in nums:
        #     if i not in x:
        #         x.add(i)
        # return len(nums) != len(x)

        # nums.sort()
        # x = set()
        # for i in nums:
        #     if i in x:
        #         return True
        #     x.add(i)
        # return False