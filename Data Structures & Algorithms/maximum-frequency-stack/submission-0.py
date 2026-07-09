from collections import Counter, defaultdict

class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Increment frequency of the value
        f = self.freq[val] + 1
        self.freq[val] = f
        
        # Update max_freq if a new peak is reached
        if f > self.max_freq:
            self.max_freq = f
            
        # Add the value to the stack corresponding to its current frequency
        self.group[f].append(val)

    def pop(self) -> int:
        # Get the most frequent element closest to the top
        val = self.group[self.max_freq].pop()
        
        # Decrement its frequency count
        self.freq[val] -= 1
        
        # If the highest frequency stack is now empty, lower the max_freq
        if not self.group[self.max_freq]:
            self.max_freq -= 1
            
        return val