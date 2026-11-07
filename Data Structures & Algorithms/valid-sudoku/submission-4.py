class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = defaultdict(set)

        for i in range(9):
            for j in range(9):
                number = board[j][i]
                rowBand = i // 3
                columnBand = j // 3
                band = f"band{rowBand}{columnBand}"
                column = f"column{i}"
                row = f"row{j}"

                if(number != '.'):
                    if(number in count[column] or number in count[row] or number in count[band]):
                        return False
                    count[column].add(number)
                    count[row].add(number)
                    count[band].add(number)

        return True