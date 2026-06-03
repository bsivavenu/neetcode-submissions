class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Step 1: Sort the people by weight
        people.sort()
        
        left = 0
        right = len(people) - 1
        boats = 0
        
        # Step 2: Pair them up using two pointers
        while left <= right:
            # If the lightest and heaviest person can fit together
            if people[left] + people[right] <= limit:
                left += 1  # Lightest person gets on the boat
            
            # The heaviest person always gets on the boat
            right -= 1
            boats += 1     # Increment the boat count
            
        return boats