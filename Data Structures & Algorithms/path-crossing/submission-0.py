class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Starting point
        x, y = 0, 0
        # Use a set for O(1) average time complexity lookups
        visited = {(x, y)}
        
        for direction in path:
            # Update the current position based on direction
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            
            # Check if we have been here before
            current_pos = (x, y)
            if current_pos in visited:
                return True
            
            # Record the new location
            visited.add(current_pos)
            
        return False