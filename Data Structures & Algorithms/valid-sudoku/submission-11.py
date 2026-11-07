class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        band = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                number = board[j][i]
                bandIndex = (i // 3) * 3 + j // 3

                if(number != '.'):
                    if(number in column[i] or number in row[j] or number in band[bandIndex]):
                        return False
                    column[i].add(number)
                    row[j].add(number)
                    band[bandIndex].add(number)

        return True