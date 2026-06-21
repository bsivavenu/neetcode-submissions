class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # This will store pairs of (index, temperature) or just indices
        
        for i, temp in enumerate(temperatures):
            # Check if current temperature is greater than the temperature at the index on top of the stack
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            
            # Push the current day's index onto the stack
            stack.append(i)
            
        return result