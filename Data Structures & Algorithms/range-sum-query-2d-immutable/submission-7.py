class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = [[0] * (len(matrix[0]) + 1)]

        for i, row in enumerate(matrix, start=1):
            s = 0
            newRow = [0]
            for j, cell in enumerate(row, start=1):
                s += cell
                print(j)
                addUp = self.sums[i - 1][j]
                newRow.append(s + addUp)
            self.sums.append(newRow)
                
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        querySum = self.sums[row2 + 1][col2 + 1]

        rowSum = self.sums[row1][col2 + 1]
        columnSum = self.sums[row2 + 1][col1]
        interSectionSum = self.sums[row1][col1]

        return querySum - rowSum - columnSum + interSectionSum
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)