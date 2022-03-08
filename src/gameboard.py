from src.board import Board


class Gameboard(Board):
    def __init__(self, rows, columns):
        '''
        Initialises the full board with the length, width and the board matrix
        Here, the board matrix is kept as public, to allow all the functions to gain a direct access to it
        Each element in the board matrix is of the form 
        '''
        super().__init__(rows, columns)



    def write_full_on_board(self, full_board, start_in):
        ''' 
        Writes from the canvas onto the gameboard from the start_in to till the screen is completely filled
        '''
        (r, _) = full_board.getdim()
        try:
            for i in range(0, r):  # all the rows from blahblahblah
                for j in range(0, self._columns):  # all the columns from teh gameboard
                    self._board[i+2][j] = full_board.getxy(i, j+start_in)
        except Exception as e:
            print(e)


    def prepare_board(self):
        self.generate_background()


    