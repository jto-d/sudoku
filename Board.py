class Board():

    def __init__(self, init_board: str):
        self.board = self.__create_board(init_board)

    def __create_board(self, init_board: str):
        
        board = []

        for line in init_board:
            line = line.strip()

            board.append([])

            for c in line:
                board[-1].append(int(c))
        return board

    def __str__(self):
        return str(self.board)