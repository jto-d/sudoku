from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

import argparse

class UI(Frame):
    def __init__(self, parent, game, margin, side):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)


        self.row, self.col = 0,0


        self.MARGIN = margin
        self.SIDE = side

        self.__initUI()


        

        
    
    def __initUI(self):

        self.WIDTH = self.HEIGHT = self.MARGIN * 2 + self.SIDE * 9

        self.parent.title("Sudoku") 
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)

        start_button = Button(self, text="Solve Puzzle",
                                command=self.__start_puzzle)
        start_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()


    def __draw_grid(self):

        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = self.MARGIN + i * self.SIDE
            y0 = self.MARGIN
            x1 = self.MARGIN + i * self.SIDE
            y1 = self.HEIGHT - self.MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = self.MARGIN
            y0 = self.MARGIN + i * self.SIDE
            x1 = self.WIDTH - self.MARGIN
            y1 = self.MARGIN + i * self.SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)


    def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game.board[i][j]
                if answer != 0:
                    x = self.MARGIN + j * self.SIDE + self.SIDE / 2
                    y = self.MARGIN + i * self.SIDE + self.SIDE / 2
                    original = self.game.init_board[i][j]
                    color = "black" if answer == original else "sea green"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )

    def __start_puzzle(self):
        self.game.solve(self)
    
    def update(self):
        self.__draw_puzzle()