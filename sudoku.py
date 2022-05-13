import argparse
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
from Board import Board


MARGIN = 20
SIDE = 50

WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

class SudokuUI(Frame):
    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)


        self.row, self.col = 0,0

        self.__initUI()
    
    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, side=TOP)

def board_setup(file_name: str):
    with open(file_name) as f:
        content = f.readlines()
        return content

FILE_NAME = "board.txt"

init_board = board_setup(FILE_NAME)

b = Board(init_board)

print(str(b))