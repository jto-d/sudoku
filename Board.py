import time

class Board():

    def __init__(self, init_board: str):
        self.board = self.__create_board(init_board)
        self.init_board = self.__create_board(init_board)

    def __create_board(self, init_board: str) -> list:
        
        board = []

        for line in init_board:
            line = line.strip()

            board.append([])

            for c in line:
                board[-1].append(int(c))
        return board

    def __str__(self):
        output = ""

        for line in self.board:
            for ind, num in enumerate(line):
                if ind == 8:
                    output += str(num) + "\n"
                else:
                    output+= str(num) + " "
        
        return output

    def find_empty(self) -> tuple:
        for row, line in enumerate(self.board):
            for col, num in enumerate(line):
                if num == 0:
                    return(row, col)
        
        return None

    def is_valid_square(self, num: int, coords: tuple) -> bool: 
        
        row, col = coords



        square = self.board[row][col]
        

        # check to see if the row is valid
        for ind, val in enumerate(self.board[row]):
            if val == num and ind != col:
                return False 

        # check to see if the column is valid
        for ind, lst in enumerate(self.board):
            if lst[col] == num and ind != row:
                return False

        # check to see if the square is valid
        y = row // 3
        x = col // 3

        for i in range(y*3, y*3+3): # iterate through the rows
            for j in range(x*3, x*3+3): # iterate through the columns
                if self.board[i][j] == num and (i,j) != coords:
                    return False
        
        return True



        
    def solve(self, gui):
        # find an empty square (assumes there is one empty square)
        empty_coords = self.find_empty()


        if not empty_coords:
            print("Board Solved!")
            
            gui.update()
            return True

        row, col = empty_coords
        # check to see if the square is valid
        for i in range(1,10):
            

            
            
            if self.is_valid_square(i, (empty_coords)):

                self.board[row][col] = i
                
                if self.solve(gui):
                    return True

                self.board[row][col] = 0

        return False
            

                
        

        
