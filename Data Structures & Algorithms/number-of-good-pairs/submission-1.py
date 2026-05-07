class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        total_pairs = 0
        for n in count.values():
            # Using the formula instead of a nested loop
            total_pairs += (n * (n - 1)) // 2
            
        return total_pairs