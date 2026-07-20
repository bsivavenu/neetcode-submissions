class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))

        x = set()
        for i in nums:
            if i not in x:
                x.add(i)
        return len(nums) != len(x)

        # m = sorted(nums)
        # x = []
        # for i in m:
        #     if i not in x:
        #         x.append(i)
        # return len(m) != len(x)