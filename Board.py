import numpy as np
import sys

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

        # print tempArray    
        """    
        for i in range( len( tempArray) ):
            for j in range( len( tempArray[i] ) ):
                print( '(' + str( i ) + ', ' + str(j) + ')' + str(tempArray[i][j] ) )
        """
        
        # flag for finishing user input
        done = False

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
                    # if the user didn't try to exit, check if they entered a number
                    if not( tmp.isdigit() ):
                        print( 'Enter a cell value form 1-9: ' )
                        continue 
                    # check if cell value from user is valid 
                    tmp = int( tmp )
                    if tmp > 0 and tmp < 10:
                        tempArray[i][j] = tmp
                        break
                    else:
                        print( 'Enter a cell value from 1-9: ' )
        
        # board
        self.board = tempArray
    
    # make sure the board entered by the user is a valid starting board configuration 
    def validateBoard( self ):
        print('nada')

    # add cell value to the board
    def add( self, i, j, value ):
        # check method parameters for validity 
        if i < 1 or i > 9:
            print( 'Add: i coordinate out of bounds' )
        elif j < 1 or j > 9: 
            print( 'Add: j coordinate out of bounds' )
        elif not( value.isdigit() ) or value < 1 or value > 9:
            print( 'Add: enter a valid value' )
        # set value at coordinate 
        self.board[i][j] = value 
        # validate that new value doesn't break the board 
        if self.validateBoard() == False:
            print( 'Add: Entered value: ' + value + ' at position (' + i + ', ' + j + ') breaks the board' )
    
    # prints the board in a pretty format
    def printBoard( self ):
        printB = np.array( self.board )
        print( printB )


        
        


