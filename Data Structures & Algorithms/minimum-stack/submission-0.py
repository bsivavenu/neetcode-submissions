class MinStack:

    def __init__(self):
        # Main stack to store all elements
        self.stack = []
        # Auxiliary stack to store the minimums at each level
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # If min_stack is empty, this val is the current minimum.
        # Otherwise, compare val with the current minimum at the top of min_stack.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]