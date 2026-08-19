from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        for i in nums:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1

        sorted_items = sorted(x.items(), key=lambda item: item[1], reverse=True)
        # print(sorted_items)
        return [i[0] for i in sorted(x.items(), key=lambda item: item[1], reverse=True)[:k]]
        # return [i for i,count in Counter(nums).most_common(k)]