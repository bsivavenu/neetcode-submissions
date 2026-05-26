class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set up pointers for nums1, nums2, and the placement position
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # Merge while there are elements in both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are any remaining elements in nums2, copy them over.
        # (If nums1 has remaining elements, they are already in the correct place!)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1