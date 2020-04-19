import numpy as np 
import sys
from Board import Board 


def solve( board ):
    # find first empty square
    find = board.findEmpty()
    # print( find ) 
    # if no empty squres, done
    if not find:
        return True
    else: 
        # set coordinates of the empty cell
        row, col = find
    # try putting values in empty square 
    for i in range( 1, 10 ):
        if board.valid( i, ( row, col ) ):
            board.add( row, col, i )
            # recursive call
            if solve( board ):
                return True
            board.add( row, col, 0)
    return False 

def main():
    # have user enter in the initial board configuration
    board = Board() 
    print( 'INITIAL BOARD:')
    board.printBoard()
    if solve( board ) == True:
        print( '------------------------------------------------------------------------------------------------------------------')
        print( 'SOLUTION: ' )
        board.printBoard()
        

if __name__ == '__main__':
    main()