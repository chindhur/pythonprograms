def print_game(board):
    for row in board:
        print("|".join(row))
        print("-"*9)
def check_winner(board,player):
    for row in board:
        row_complete=True
        for cell in row:

            if row_complete!=player:
                row_complete=False
                break
        if row_complete:
            return True

    for col in range(3):
        col_complete=True
        for row in range(3):
            if board[row][col]!=player:
                col_complete=False
                break
        if col_complete:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2]==board[1][1]==board[2][0]==player:
        return True
    else:
        return False


def play_game():
    board=[[" "for _ in range(3)]for _ in range(3)]
    current_player = "x"

    while True:
         print_game(board)
         row=int(input("enter the row:"))
         col=int(input("enter the column:"))

         if board[row][col] != " ":
             print("invalid move try again")
             continue
         board[row][col]=current_player
         if check_winner(board, current_player):
             print(board)
             print(f"Player current_player wins")
             break
         if all(cell != " " for row in board for cell in row):
             print_game(board)
             current_player="o" if current_player=="x" else "x"
play_game()








