from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # Get the current size of the queue before adding the new element
        size = len(self.queue)
        
        # Add the new element to the back of the queue
        self.queue.append(x)
        
        # Rotate the queue so that the newly added element comes to the front
        for _ in range(size):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on the top of the stack and returns it.
        """
        # The front of our queue always represents the top of the stack
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        # The front of our queue is the top of the stack
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0