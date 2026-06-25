class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up position and speed, then sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        
        for pos, spd in cars:
            # Calculate the time needed to reach the target for the current car
            time = (target - pos) / spd
            
            # If stack is not empty and current car's time is <= the car ahead's time,
            # it means this car will catch up and join the fleet ahead.
            # Otherwise, it forms a new fleet, so we push its time onto the stack.
            if not stack or time > stack[-1]:
                stack.append(time)
                
        # The number of unique fleet lead times remaining in the stack is our answer
        return len(stack)