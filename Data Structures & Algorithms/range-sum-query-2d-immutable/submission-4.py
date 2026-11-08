class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = [[] for _ in range(len(matrix) + 1)]

        for i in range(len(matrix) + 1):
            row = matrix[i - 1]
            s = 0
            for j in range(len(row) + 1):
                if(i == 0 or j == 0):
                    self.sums[i].append(0)
                else:
                    cell = row[j - 1]
                    s += cell

                    addUp = 0
                    if(i != 0):
                        addUp = self.sums[i - 1][j]

                    self.sums[i].append(s + addUp)
                
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        querySum = self.sums[row2 + 1][col2 + 1]

        rowSum = self.sums[row1][col2 + 1]
        columnSum = self.sums[row2 + 1][col1]
        interSectionSum = self.sums[row1][col1]

        return querySum - rowSum - columnSum + interSectionSum
        

# 38 total -24-14 + 3 + 5 = 8
# 24 top right cell (1, 3)
# 14 left bottom cell (4, 0)
# 3 + 5 -> intersection from 0, 0

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)