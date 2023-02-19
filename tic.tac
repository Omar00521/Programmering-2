Tic Tac Tow

def won(board):
    for row in board:
        if all(x == "X" for x in row):
            return True
        if all(x == "O" for x in row):
            return True
    for i in range(len(board)):
        if all(board[j][i] == "X" for j in range(len(board))):
            return True
        if all(board[j][i] == "Y" for j in range(len(board))):
            return True
        

Player1 = []
Player2 = []

print ("Welcome!")

Player1=input("state your name player 1!")


Player2=input("and what would your name be player 2?")


def print_board(board):
    for row in board:
        print(*row)
    print("1 2 3 4 5 6 7")


rows = 6
cols = 7

board = [["_" for _ in range(cols)]for _ in range(rows)]
print_board(board)
play_again= True
while play_again:
    print ("your turn player 1")
    choice_row=int(input("Vwhich row do you want to cross over?")) - 1
    choice_cols=int(input("which column do you want to cross over?")) -1

    board[choice_row][choice_cols] = "X"
    won(board)
    print_board(board)

    print ("Your turn player 2")
    choice_row=int(input("Vwhich row do you want to cross over?")) - 1
    choice_cols=int(input("which column do you want to cross over?")) -1 
    
    board[choice_row][choice_cols] = "Y"
    won(board)
    print_board(board)
    
