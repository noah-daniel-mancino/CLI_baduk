from typing import Callable

class Board:
    '''
    Class used to represent a rectanglular Go board.
    '''
    def __init__(self, dim=9) -> None:
        # Empty = 0, White = 1, Black = 2
        self.board = [[0 for x in range(dim)] for x in range(dim)]
        # We want to keep the last board in memory for undos and kos. 
        self.last_board = self.board
        self.black_score = 0
        self.white_score = 0


    def move(self, cords: tuple, color: int) -> bool:
        if self.valid_move(cords, color):
            self.board[cords[0]][cords[1]] = color
            return True
        return False

    def valid_move(cords: tuple, color: int) -> bool:
        '''
        Input:
        Cords - The x and y coordinates where the stones are to be placed.
        Color - Color of the placed stone.

        Returns:
        True for valid moves and False for invalid moves.
        '''
        # First, simply check if the space is already occupied.
        if self.board[cords[0]][cords[1]] != 0:
            return False
        # Next, check if the move leaves any liberties in the group. To do
        # this, we will temporarily place the stone, but the board should be
        # returned to it's previous state on function exit. 
        self.board[cords[0]][cords[1]] = color
        # Next, we check for ko. This board only enforces the simplest ko rule,
        # namely, that consecutive terms cannot repeat board states. 
        if self.board == self.last_board:
            return False

    def _group_search(cords: tuple, group_func: Callable) -> list:
        '''
        Description:
        Counting and checking for liberties both call for performing some
        computation on every member of a group. This function will search
        through the group using flood fill, and apply group_func to each
        stone along the way. 

        Input:
        Cords - The x and y coordinates of an arbitrary element of the group.
        group_func - The function to apply to each.

        Returns:
        A list containing the each output from group_func.
        '''

    def count_territory(cords: tuple) -> int:
        pass
    
    def check_vitals(cords: tuple) -> bool:
        pass

    def undo(self):
        self.board = self.last_board


