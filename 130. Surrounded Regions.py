class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            pass
        else:
        
            #checking if there is 'S' arount current char
            def up(row, col):
                return board[row - 1][col] == 'S'

            def down(row, col):
                return board[row + 1][col] == 'S'

            def left(row, col):
                return board[row][col - 1] == 'S'

            def right(row, col):
                return board[row][col + 1] == 'S'


            #turning all edge 'O' to 'S'
            for i in [0, len(board) - 1]:
                for j in range(len(board[0])):
                    if board[i][j] == 'O':
                        board[i][j] = 'S'

            for i in [0, len(board[0]) - 1]:
                for j in range(len(board)):
                    if board[j][i] == 'O':
                        board[j][i] = 'S'

            #checking inside if there is connection between 'O' and 'S'

            temp = 0
            n = 1
            while n == 1:

                for i in range(1, len(board) - 1):
                    for j in range(1, len(board[i]) - 1):

                        if board[i][j] == 'O':
                            if up(i, j) or down(i,j) or left(i,j) or right(i,j):
                                board[i][j] = 'S'
                                temp += 1

                #if there is a change from 'O' to 'S', do everything again                
                if temp > 0:
                    n = 1
                else:
                    n = 0
                temp = 0

            #changing every remaining 'O' with 'X', and all safe ones 'S' with 'O'
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    if board[i][j] == 'S':
                        board[i][j] = 'O'
