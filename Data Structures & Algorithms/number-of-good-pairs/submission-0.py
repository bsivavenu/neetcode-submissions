class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        x = [] 
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    x.append((i,j))
        return len(x)