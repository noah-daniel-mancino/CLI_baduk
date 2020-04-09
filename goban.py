'''
Author: Noah Mancino
'''
from typing import Callable
from termcolor import colored

class Board:
    '''
    Class used to represent a rectanglular Go board.
    '''
    def __init__(self, dim=9) -> None:
        '''
        Description: 
        Constructor for board object.

        Input:
        dim - The dimension of the game board.

        Notes:
        The dimension must be less than 26, because one axis is labled using
        english alphebetic characters.
        '''
        try:
            assert 0 < dim <= 26
            assert isinstance(dim, int)
        except AssertionError:
            print('Please choose a dimension between 0 and 26')
            return

        # Empty = 0, White = 1, Black = 2
        self.board = [[0 for x in range(dim)] for x in range(dim)]
        self.board[3][3] = 1
        self.board[2][2] = 2
        self.board[15][2] = 1
        # We want to keep the last board in memory for undos and kos. 
        self.last_board = self.board
        self.dim = dim
        self.black_score = 0
        self.white_score = 0

    def move(self, cords: tuple, color: int) -> bool:
        '''
        Make a move, brother
        '''
        # if self.valid_move(cords, color):
        #     self.board[cords[0]][cords[1]] = color
        #     self._group_search(cords, self.is_dead)
        #     return True
        # return False

    def valid_move(self, cords: tuple, color: int) -> bool:
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
        # this, we will need to modify a copy of the board.
        board_copy = copy.deepcopy(self.board)
        self.board[cords[0]][cords[1]] = color
        # Next, we check for ko. This board only enforces the simplest ko rule,
        # namely, that consecutive terms cannot repeat board states. 
        if self.board == self.last_board:
            return False

    def _group_search(self, cords: tuple, group_func: Callable, 
                      stop_cond=lambda x: False) -> list:
        '''
        Description:
        Methods involving checking for liberties call for performing some
        computation on every member of a group or territory. This function will search
        through the group using flood fill, and apply group_func to each
        stone along the way. If group_func returns a value fulfilling the stop
        condition set by stop_cond, the function will exit early. This is 
        useful in cases where you are looking to see if any one stone meets 
        some requirement, e.g a group is not dead if any member has a liberty. 

        Input:
        Cords - The x and y coordinates of an arbitrary element of the group.
        group_func - The function to apply to each.
        stop_cond - Optional. A bool valued function that will end the search
        if it returns True when applied to the output of group_func.

        Returns:
        A list containing the output from each call to group_func.
        '''
        return 

    def count_territory(self, cords: tuple) -> int:
        '''
        Returns:
        Territory
        '''
        return 
    
    def is_dead(self, cords: tuple) -> bool:
        '''
        Description:
        Checks if a group is alive or not. Returns true if so and false
        otherwise.

        Input:
        cords - Coordinate of any member of a group

        Returns:
        True if group is alive, false if the group is dead. 
        '''
        return

    def is_living(self, cords: tuple) -> bool:
        '''
        Description:
        Checks if a group has two seprate pieces of eyespace. This function is
        fairly naive, and is only intended to be used at the end of games when
        everything that can be invaded has been and all false eyes have been popped.
        Used so that the players do not need to be asked about the status of
        each group when it is time to score, which can be quite tedious.

        Input:
        cords - Coordinates of any member of a group

        Returns:
        True if there are two pieces of eye-space (even if the eyespace is
        false), and False otherwise.

        TODO: Check for False eyes. This can be done by checking that each 
        group bordering potential eye space has two eyes, flagging groups that
        have already been checked. 
        '''
        return
    
    def undo(self) -> None:
        '''
        Description:
        Undoes last move.
        '''
        self.board = self.last_board

    def __str__(self) -> str:
        '''
        Returns:
        A string representation of the game board.
        '''
        # String reprentations of individual spaces.
        space_strs = {0: 'x', 1: colored('W', 'blue'), 2: colored('B', 'red')}
        # We only need the first self.dim lables, and each character comes
        # with a space so the index needs to be doubled
        bottom_labels = (' A B C D E F G H I J K L M N ' 
                         'O P Q R S T U V W X Y Z')[:self.dim * 2]
        # The board, represented as a string.
        board_str = ''
        for index, row in enumerate(self.board):
            row_str = ''
            for space in row:
                row_str += space_strs[space] + ' '
            side_label = str(index + 1).rjust(2)
            board_str += f'{side_label}  {row_str}  {side_label}\n'
        board_str += f'\n   {bottom_labels}   '
        return board_str

    def in_bounds(self, cords: tuple) -> bool:
        '''
        Returns:
        True if coordinates are in the board, and False otherwise.
        '''
        return 0 <= cords[0] < self.dim and 0 <= cords[1] < self.dim

        
BOARD = Board(19)
print(str(BOARD))
