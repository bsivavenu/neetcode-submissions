class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        
        for log in logs:
            if log == "../":
                # Move to parent folder, but don't go below the main folder (0)
                if depth > 0:
                    depth -= 1
            elif log == "./":
                # Remain in the same folder, do nothing
                continue
            else:
                # Move to a child folder, increase depth
                depth += 1
                
        return depth