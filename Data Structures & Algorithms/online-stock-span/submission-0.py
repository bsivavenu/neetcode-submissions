class StockSpanner:

    def __init__(self):
        # The stack will store tuples of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        # Every day has an initial span of at least 1 (itself)
        span = 1
        
        # Pop from the stack while the top element's price is <= today's price
        while self.stack and self.stack[-1][0] <= price:
            # Add the span of the lower/equal price day to the current span
            span += self.stack.pop()[1]
            
        # Push the current price and its calculated span onto the stack
        self.stack.append((price, span))
        
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)