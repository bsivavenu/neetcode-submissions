class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Step 1: Count the frequency of each integer
        counts = Counter(arr)
        
        # Step 2: Initialize our result to -1
        max_lucky = -1
        
        # Step 3: Iterate through the unique numbers and their frequencies
        for num, freq in counts.items():
            # A number is lucky if its value equals its frequency
            if num == freq:
                # We want the largest one
                if num > max_lucky:
                    max_lucky = num
                    
        return max_lucky