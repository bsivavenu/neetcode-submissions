class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x, y = 0, 0
        for i in range(len(path)):
            visited.add((x,y))
            
            if path[i] == 'N':
                y += 1
            elif path[i] == 'E':
                x += 1
            elif path[i] == 'W':
                x -= 1
            elif path[i] == 'S':
                y -= 1
            
            if (x,y) in visited:
                return True
        
        return False