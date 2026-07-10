class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            if op == '+':
                # Sum of the previous two scores
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                # Double the previous score
                stack.append(stack[-1] * 2)
            elif op == 'C':
                # Invalidate/remove the previous score
                stack.pop()
            else:
                # It's an integer score, convert and push to stack
                stack.append(int(op))
                
        return sum(stack)