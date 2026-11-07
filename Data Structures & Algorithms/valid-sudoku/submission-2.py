class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = []
        boxes = []

        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(board[j][i])
            columns.append(temp)


        for l in range(3):
            for k in range(3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[3*l + i][3*k + j])

                boxes.append(box)

        for i in range(9):
            for j in range(9):
                number = j + 1
                count = 0
                
                for num in columns[i]:
                    if (num != '.' and int(num) == number):
                        count += 1
                        if(count == 2):
                            return False
                
                count = 0
                
                for num in board[i]:
                    if (num != '.' and int(num) == number):
                        count += 1
                        if(count == 2):
                            return False

                count = 0

                for num in boxes[i]:
                    if (num != '.' and int(num) == number):
                        count += 1
                        if(count == 2):
                            return False

        return True
