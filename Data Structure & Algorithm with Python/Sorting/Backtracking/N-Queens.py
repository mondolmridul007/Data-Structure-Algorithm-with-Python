def IsBoardOk(chessboard, row, col):
    # Check if there is a queen 'Q' positioned to the left of column col on the same row.
   for c in range(col):
       if (chessboard[row][c] == 'Q'):
           return False
   # Check if there is queen 'Q' positioned on the upper left diagonal
   for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
       if (chessboard[r][c] == 'Q'):
           return False
    # Check if there is queen 'Q' positioned on the lower left diagonal
   for r, c in zip(range(row+1, len(chessboard), 1), range(col-1, -1, -1)):
      if (chessboard[r][c] == 'Q'):
          return False
   return True

def DisplayBoard(chessboard):
    displaysolution=[]
    for row in chessboard:
        displaysolution.append(row.index('Q')+1)
    print(*displaysolution, sep=" ")

def PlaceNQueens (chessboard, col):
    if (col >= len(chessboard)):
        print("Solution: ")
        DisplayBoard(chessboard)
    else:
        for row in range(len(chessboard)):    
            chessboard[row][col] = 'Q'
            if (IsBoardOk(chessboard, row, col) == True):
                PlaceNQueens(chessboard, col + 1)
            chessboard[row][col] = '.'

chessboard = []
N = int(input("Sample input: "))
for i in range(N) :
    row = ["."] * N
    chessboard.append(row)
PlaceNQueens(chessboard, 0)