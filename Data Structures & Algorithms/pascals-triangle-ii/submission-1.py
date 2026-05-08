class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # The first element of any row is always 1
        row = [1]
        
        # We compute the next element based on the previous one:
        # next_val = prev_val * (rowIndex - i) / (i + 1)
        for i in range(rowIndex):
            # Using integer division to keep it clean
            next_val = row[-1] * (rowIndex - i) // (i + 1)
            row.append(next_val)
            
        return row