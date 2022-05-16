from tkinter import Tk
from Board import Board
from UI import UI

MARGIN = 50
SIDE = 40

def board_setup(file_name: str):
    with open(file_name) as f:
        content = f.readlines()
        return content

FILE_NAME = "board.txt"

init_board = board_setup(FILE_NAME)

b = Board(init_board)


root = Tk()
game = UI(root, b, MARGIN, SIDE)

root.mainloop()






