class Game:
    '''
    Board layout: 0 1  2  3  4  5  6  7
                  0 13 12 11 10 9  8  7

    Each player starts with 24 on their side.
    Player 1 can pick from 1 through 6
    Player 2 can pick from 8 through 13
    '''
    def __init__(self):
        self.board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]

    def isDone(self):
        return sum(self.board[1:7]) == 0 or sum(self.board[8:]) == 0