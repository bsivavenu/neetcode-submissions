from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # x = {}
        # for i in nums:
        #     if i in x:
        #         x[i] += 1
        #     else:
        #         x[i] = 1

        ############
        x = Counter(nums)
        # return sorted(x, key=lambda item: x[item], reverse=True)[:k]

        ####################
        # return [i for i,count in Counter(nums).most_common(k)]

        #############

        heap = []
        for i,j in x.items():
            heapq.heappush(heap,(j,i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i for j,i in heap]