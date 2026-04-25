class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        x = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i :
                    row.append(1)
                else:
                    value = x[i-1][j-1]+ x[i-1][j]
                    row.append(value)
            x.append(row)

        return x