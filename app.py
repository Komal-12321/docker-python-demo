print("Hello from Docker + CodeBuild 🚀")

print("Running a simple Tic Tac Toe board:")

board = [" "] * 9

def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Simulate a few moves
board[0] = "X"
board[4] = "O"
board[8] = "X"

display_board()

print("Game simulation complete ✅")
