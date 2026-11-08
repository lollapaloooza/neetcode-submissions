class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.length = len(matrix)
        self.sums = [[] for _ in range(self.length)]

        for i in range(self.length):
            row = matrix[i]
            s = 0
            for j in range(len(row)):
                cell = row[j]
                s += cell

                addUp = 0
                if(i != 0):
                    addUp = self.sums[i - 1][j]

                self.sums[i].append(s + addUp)
                
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        querySum = self.sums[row2][col2]

        rowSum = 0
        columnSum = 0
        interSectionSum = 0

        if(col1 > 0 and row1 > 0):
            interSectionSum = self.sums[row1 - 1][col1 - 1]

        if(col1 > 0):
            columnSum = self.sums[row2][col1 - 1]

        if(row1 > 0):
            rowSum = self.sums[row1 - 1][col2]

        print(querySum, rowSum, columnSum, interSectionSum)
        return querySum - rowSum - columnSum + interSectionSum
        

# 38 total -24-14 + 3 + 5 = 8
# 24 top right cell (1, 3)
# 14 left bottom cell (4, 0)
# 3 + 5 -> intersection from 0, 0

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)