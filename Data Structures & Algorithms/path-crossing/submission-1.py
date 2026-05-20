class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Track current coordinates
        x, y = 0, 0
        
        # Store visited locations as tuples for fast O(1) lookups
        visited = {(0, 0)}
        
        # Map directions to coordinate changes
        moves = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }
        
        for direction in path:
            dx, dy = moves[direction]
            x += dx
            y += dy
            
            # If the new position is already in our history, the path crossed
            if (x, y) in visited:
                return True
                
            # Otherwise, log the visit and keep moving
            visited.add((x, y))
            
        return False