# Implement Tic Tac Toe game using state space search.

board = [' ']*9

def show():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

def check(p):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in win)

for i in range(9):
    show()
    
    player = 'X' if i % 2 == 0 else 'O'
    move = int(input(f"Player {player}, enter position (0-8): "))

    if board[move] != ' ':
        print("Invalid move, try again")
        continue

    board[move] = player

    if check(player):
        show()
        print(f"Player {player} wins!")
        break   
else:
    show()
    print("Game Draw")