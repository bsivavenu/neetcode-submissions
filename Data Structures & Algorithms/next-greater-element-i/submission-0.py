class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                small_element = stack.pop()
                x[small_element] = num

            stack.append(num)

        return [x.get(n,-1) for n in nums1]