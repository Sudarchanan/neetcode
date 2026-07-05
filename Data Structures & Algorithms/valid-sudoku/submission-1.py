class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        boardLenghth = 9


        for row in range(boardLenghth):
            seenSet  = set()

            for i in range(boardLenghth):
                
                if board[row][i] == '.':
                    continue

                if board[row][i]  in seenSet:
                    return False
                
                seenSet.add(board[row][i])

        for col in range(boardLenghth):
            seenSet  = set()

            for i in range(boardLenghth):

                if board[i][col] == '.':
                    continue

                if  board[i][col]  in seenSet:
                    return False
                
                seenSet.add( board[i][col])

        
        for square in range(boardLenghth):
            seenSet  = set()

            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seenSet:
                        return False
                    seenSet.add(board[row][col])
        return True

        

