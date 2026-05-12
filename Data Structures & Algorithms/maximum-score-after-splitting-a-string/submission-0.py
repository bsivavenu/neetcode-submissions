class Solution:
    def maxScore(self, s: str) -> int:
        # Initial counts
        total_ones = s.count('1')
        left_zeros = 0
        right_ones = total_ones
        max_score = 0
        
        # Iterate through the string, stopping before the last character
        # to ensure the right substring is non-empty.
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            
            # Calculate score at this split point
            current_score = left_zeros + right_ones
            max_score = max(max_score, current_score)
            
        return max_score