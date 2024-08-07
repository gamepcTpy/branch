from board import Board
from ui import print_board
from move import move

class Game:
    def __init__(self):
        self.board = Board()

    def start(self):
        while self.board.can_move():
            print_board(self.board.grid)
            move_input = input("Enter move (w/a/s/d): ").strip().lower()
            if move_input in 'wasd':
                move(self.board, move_input)
                self.board.add_new_tile()
            else:
                print("Invalid move! Please enter w/a/s/d.")
        print("Game Over!")
        print_board(self.board.grid)
