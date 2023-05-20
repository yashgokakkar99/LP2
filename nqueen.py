def issafe(board, row,col, n):

    for i in range(row):
        if(board[i][col] == 1):
            return False
    
    i = row
    j = col

    while(i>=0 and j>=0):
        if(board[i][j]==1):
            return False
        
        i-=1
        j-=1

    i = row
    j = col

    while i>=0 and j<n:
        if(board[i][j]==1):
            return False
        
        i-=1
        j+=1

    return True

def solve_n_queen(board, row, n):

    if row==n:
        return True
    
    for col in range(n):

        if issafe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queen(board, row+1, n):
                return True
            
        board[row][col] = 0
    return False


def main():
    n = int(input("Enter number of queens : "))
    board = [[0]*n for _ in range(n)]

    if solve_n_queen(board, 0, n):
        for row in board:
            print(*row)
    else:
        print("No solution")


if __name__ == '__main__':
    main()

    
