class Solution:

    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                # Record a new score that is the sum of the previous two scores
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # Record a new score that is the double of the previous score
                stack.append(stack[-1] * 2)
            elif op == "C":
                # Invalidate the previous score, removing it from the record
                stack.pop()
            else:
                # op is an integer, record the new score
                stack.append(int(op))

        # Return the sum of all scores remaining in the record
        return sum(stack)