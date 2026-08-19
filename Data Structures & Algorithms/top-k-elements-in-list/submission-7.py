from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        for i in nums:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1

        return sorted(x, key=lambda item: x[item], reverse=True)[:k]

        ####################
        # return [i for i,count in Counter(nums).most_common(k)]