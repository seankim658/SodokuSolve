import numpy as np
import sys

builtIn = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0],
]

class Board: 
    
    # constructor 
    def __init__(self):

        # give user instructions for entering board
        print( '------------------------------------------------------------------------------------------------------------------')
        print( 'INSTRUCTIONS' ) 
        print( 'Enter "Exit" to quit' )
        print( 'Enter "Done" to finish board (leaves rest of board as empty cells)' )
        print( 'Enter each board space value going right to left and up to down (enter "0" for empty squares): ' )
        
        # create temporary 2D python array of user input 
        n = 9
        tempArray = [[0 for k in range( n )] for j in range( n )]
        
        # flag for finishing user input and using built in board
        done = False
        useBuiltIn = False

        # prompt user to enter in each cell value for the table 
        for i in range( len( tempArray ) ):

            if done == True:
                break

            for j in range( len( tempArray[i] ) ):
                
                if done == True:
                    break

                while True:
                    # grab cell value from user
                    tmp = input( 'Enter value for cell (' + str( i ) + ', ' + str( j ) + '): ' )
                    # check if user is trying to exit 
                    if tmp == "Exit" or tmp == "exit":
                        sys.exit( 0 ) 
                    elif tmp == "Done" or tmp == "done":
                        done = True 
                        break
                    elif tmp == 'built in':
                        done = True
                        useBuiltIn = True
                        break
                    # if the user didn't try to exit, check if they entered a number
                    if not( tmp.isdigit() ):
                        print( 'Enter a cell value form 0-9' )
                        continue 
                    # check if cell value from user is valid 
                    tmp = int( tmp )
                    if tmp >= 0 and tmp < 10:
                        tempArray[i][j] = tmp
                        break
                    else:
                        print( 'Enter a cell value from 0-9' )
        
        # board
        if useBuiltIn == True:
            self.board = builtIn
        else:
            self.board = tempArray
        if self.validateInitBoard() == False:
            print( 'INVALID INITIAL BOARD CONFIGURATION' )
            self.printBoard()
            sys.exit( 1 )
    
    # validate the entered initial board configuration 
    def validateInitBoard( self ):
        for i in range( len( self.board ) ):
            for j in range( len( self.board[i] ) ):
                if self.board[i][j] != 0:
                    if self.valid( self.board[i][j], ( i, j ) ) == False:
                        return False
        return True

    # make sure the board entered by the user is a valid starting board configuration 
    def valid( self, value, pos ):
        # check indices 
        if pos[0] < 0 or pos[0] > 9:
            print( 'Row coordinate out of bounds' )
            return False 
        elif pos[1] < 0 or pos[1] > 9: 
            print( 'Col coordinate out of bounds' )
            return False
        elif value < 0 or value > 9:
            print( 'Enter a valid value' ) 
            return False

        # check row 
        for i in range( len( self.board[0] ) ):
            if self.board[pos[0]][i] == value and pos[1] != i:
                return False
        
        # check column
        for i in range( len( self.board ) ):
            if self.board[i][pos[1]] == value and pos[0] != i:
                return False

        # check subsquare
        box_X = pos[1] // 3
        box_Y = pos[0] // 3
        for i in range( box_Y * 3, box_Y * 3 + 3 ):
            for j in range( box_X * 3, box_X * 3 + 3 ):
                if self.board[i][j] == value and ( i, j ) != pos:
                    return False

        # passed all validation tests, good to add
        return True  

    # find next empty square on the board
    def findEmpty( self ):
        for i in range( len( self.board ) ):
            for j in range( len( self.board[i] ) ):
                if self.board[i][j] == 0:
                    return ( i, j )
        return False

    # add cell value to the board; returns True if the value was added and False if not
    def add( self, i, j, value ):
        # set value at coordinate if it is valid
        self.board[i][j] = value 
    
    # prints the board in a pretty format w/subgrids 
    def printBoard( self ):
         # print board        
        print( 'BOARD: ')
        for i in range( len( self.board) ):
            if i % 3 == 0 and i != 0:
                print( '------------------------')
            for j in range( len( self.board[i] ) ):
                if j % 3 == 0 and j != 0:
                    print( ' | ', end = '' ) 
                if j == 8:
                    print( self.board[i][j] )
                else:
                    print( str(self.board[i][j] ) + ' ', end = '' )
        