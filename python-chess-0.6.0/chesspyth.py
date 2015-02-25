from __future__ import print_function
import chess, numpy
import chess.pgn
from PIL import Image, ImageDraw, ImageFont

## Assigns color names to the corresponding names in the code
white = chess.WHITE
black = chess.BLACK

## Length in pixels of one side of one square
s = 64

rows1357 = [[(s*0,s*7),(s*1,s*8)],[(s*1,s*7),(s*2,s*8)],[(s*2,s*7),(s*3,s*8)],[(s*3,s*7),(s*4,s*8)],[(s*4,s*7),(s*5,s*8)],[(s*5,s*7),(s*6,s*8)],[(s*6,s*7),(s*7,s*8)],[(s*7,s*7),(s*8,s*8)],
            [(s*0,s*5),(s*1,s*6)],[(s*1,s*5),(s*2,s*6)],[(s*2,s*5),(s*3,s*6)],[(s*3,s*5),(s*4,s*6)],[(s*4,s*5),(s*5,s*6)],[(s*5,s*5),(s*6,s*6)],[(s*6,s*5),(s*7,s*6)],[(s*7,s*5),(s*8,s*6)],
            [(s*0,s*3),(s*1,s*4)],[(s*1,s*3),(s*2,s*4)],[(s*2,s*3),(s*3,s*4)],[(s*3,s*3),(s*4,s*4)],[(s*4,s*3),(s*5,s*4)],[(s*5,s*3),(s*6,s*4)],[(s*6,s*3),(s*7,s*4)],[(s*7,s*3),(s*8,s*4)],
            [(s*0,s*1),(s*1,s*2)],[(s*1,s*1),(s*2,s*2)],[(s*2,s*1),(s*3,s*2)],[(s*3,s*1),(s*4,s*2)],[(s*4,s*1),(s*5,s*2)],[(s*5,s*1),(s*6,s*2)],[(s*6,s*1),(s*7,s*2)],[(s*7,s*1),(s*8,s*2)]]
rows2468 = [[(s*0,s*6),(s*1,s*7)],[(s*1,s*6),(s*2,s*7)],[(s*2,s*6),(s*3,s*7)],[(s*3,s*6),(s*4,s*7)],[(s*4,s*6),(s*5,s*7)],[(s*5,s*6),(s*6,s*7)],[(s*6,s*6),(s*7,s*7)],[(s*7,s*6),(s*8,s*7)],
            [(s*0,s*4),(s*1,s*5)],[(s*1,s*4),(s*2,s*5)],[(s*2,s*4),(s*3,s*5)],[(s*3,s*4),(s*4,s*5)],[(s*4,s*4),(s*5,s*5)],[(s*5,s*4),(s*6,s*5)],[(s*6,s*4),(s*7,s*5)],[(s*7,s*4),(s*8,s*5)],
            [(s*0,s*2),(s*1,s*3)],[(s*1,s*2),(s*2,s*3)],[(s*2,s*2),(s*3,s*3)],[(s*3,s*2),(s*4,s*3)],[(s*4,s*2),(s*5,s*3)],[(s*5,s*2),(s*6,s*3)],[(s*6,s*2),(s*7,s*3)],[(s*7,s*2),(s*8,s*3)],
            [(s*0,s*0),(s*1,s*1)],[(s*1,s*0),(s*2,s*1)],[(s*2,s*0),(s*3,s*1)],[(s*3,s*0),(s*4,s*1)],[(s*4,s*0),(s*5,s*1)],[(s*5,s*0),(s*6,s*1)],[(s*6,s*0),(s*7,s*1)],[(s*7,s*0),(s*8,s*1)]]

influence = {chess.A8:0, chess.B8:0, chess.C8:0, chess.D8:0, chess.E8:0, chess.F8:0, chess.G8:0, chess.H8:0, 
             chess.A7:0, chess.B7:0, chess.C7:0, chess.D7:0, chess.E7:0, chess.F7:0, chess.G7:0, chess.H7:0, 
             chess.A6:0, chess.B6:0, chess.C6:0, chess.D6:0, chess.E6:0, chess.F6:0, chess.G6:0, chess.H6:0, 
             chess.A5:0, chess.B5:0, chess.C5:0, chess.D5:0, chess.E5:0, chess.F5:0, chess.G5:0, chess.H5:0, 
             chess.A4:0, chess.B4:0, chess.C4:0, chess.D4:0, chess.E4:0, chess.F4:0, chess.G4:0, chess.H4:0, 
             chess.A3:0, chess.B3:0, chess.C3:0, chess.D3:0, chess.E3:0, chess.F3:0, chess.G3:0, chess.H3:0, 
             chess.A2:0, chess.B2:0, chess.C2:0, chess.D2:0, chess.E2:0, chess.F2:0, chess.G2:0, chess.H2:0, 
             chess.A1:0, chess.B1:0, chess.C1:0, chess.D1:0, chess.E1:0, chess.F1:0, chess.G1:0, chess.H1:0}

squares = {chess.A8:[(s*0,s*7),(s*1,s*8)], chess.B8:[(s*1,s*7),(s*2,s*8)], chess.C8:[(s*2,s*7),(s*3,s*8)], chess.D8:[(s*3,s*7),(s*4,s*8)], chess.E8:[(s*4,s*7),(s*5,s*8)], chess.F8:[(s*5,s*7),(s*6,s*8)], chess.G8:[(s*6,s*7),(s*7,s*8)], chess.H8:[(s*7,s*7),(s*8,s*8)],
           chess.A7:[(s*0,s*6),(s*1,s*7)], chess.B7:[(s*1,s*6),(s*2,s*7)], chess.C7:[(s*2,s*6),(s*3,s*7)], chess.D7:[(s*3,s*6),(s*4,s*6)], chess.E7:[(s*4,s*6),(s*5,s*7)], chess.F7:[(s*5,s*6),(s*6,s*7)], chess.G7:[(s*6,s*6),(s*7,s*7)], chess.H7:[(s*7,s*6),(s*8,s*7)],
           chess.A6:[(s*0,s*5),(s*1,s*6)], chess.B6:[(s*1,s*5),(s*2,s*6)], chess.C6:[(s*2,s*5),(s*3,s*6)], chess.D6:[(s*3,s*5),(s*4,s*6)], chess.E6:[(s*4,s*5),(s*5,s*6)], chess.F6:[(s*5,s*5),(s*6,s*6)], chess.G6:[(s*6,s*5),(s*7,s*6)], chess.H6:[(s*7,s*5),(s*8,s*6)],
           chess.A5:[(s*0,s*4),(s*1,s*5)], chess.B5:[(s*1,s*4),(s*2,s*5)], chess.C5:[(s*2,s*4),(s*3,s*5)], chess.D5:[(s*3,s*4),(s*4,s*5)], chess.E5:[(s*4,s*4),(s*5,s*5)], chess.F5:[(s*5,s*4),(s*6,s*5)], chess.G5:[(s*6,s*4),(s*7,s*5)], chess.H5:[(s*7,s*4),(s*8,s*5)],
           chess.A4:[(s*0,s*3),(s*1,s*4)], chess.B4:[(s*1,s*3),(s*2,s*4)], chess.C4:[(s*2,s*3),(s*3,s*4)], chess.D4:[(s*3,s*3),(s*4,s*4)], chess.E4:[(s*4,s*3),(s*5,s*4)], chess.F4:[(s*5,s*3),(s*6,s*4)], chess.G4:[(s*6,s*3),(s*7,s*4)], chess.H4:[(s*7,s*3),(s*8,s*4)],
           chess.A3:[(s*0,s*2),(s*1,s*3)], chess.B3:[(s*1,s*2),(s*2,s*3)], chess.C3:[(s*2,s*2),(s*3,s*3)], chess.D3:[(s*3,s*2),(s*4,s*3)], chess.E3:[(s*4,s*2),(s*5,s*3)], chess.F3:[(s*5,s*2),(s*6,s*3)], chess.G3:[(s*6,s*2),(s*7,s*3)], chess.H3:[(s*7,s*2),(s*8,s*3)],
           chess.A2:[(s*0,s*1),(s*1,s*2)], chess.B2:[(s*1,s*1),(s*2,s*2)], chess.C2:[(s*2,s*1),(s*3,s*2)], chess.D2:[(s*3,s*1),(s*4,s*2)], chess.E2:[(s*4,s*1),(s*5,s*2)], chess.F2:[(s*5,s*1),(s*6,s*2)], chess.G2:[(s*6,s*1),(s*7,s*2)], chess.H2:[(s*7,s*1),(s*8,s*2)],
           chess.A1:[(s*0,s*0),(s*1,s*1)], chess.B1:[(s*1,s*0),(s*2,s*1)], chess.C1:[(s*2,s*0),(s*3,s*1)], chess.D1:[(s*3,s*0),(s*4,s*1)], chess.E1:[(s*4,s*0),(s*5,s*1)], chess.F1:[(s*5,s*0),(s*6,s*1)], chess.G1:[(s*6,s*0),(s*7,s*1)], chess.H1:[(s*7,s*0),(s*8,s*1)]}
turn = "First turn"

def readBoard(fileName):

    pgn = open (fileName)
    node = chess.pgn.read_game(pgn)
    if turn == "First turn":    
        return node.board()
    node.board().san(node.variation (0).move)
    node = node.variation (0)
    turn = 1
    return node.board()


#The parameter of this function is the turn's specified position passed into a Bitboard, 
#an object representation of a chess game at a specified turn defined by the python-chess
#library. 
def makeInfluenceMatrices(bitboard):

    #Initialize each influence matrix, i.e 8x8 matrices of 0's
    winf = numpy.zeros((8,8))
    binf = numpy.zeros((8,8))
	
    #Iterate over the entire Bitboard, tile by tile, to find all the possible attacks.
    #This process requires its own function as the Bitboard class starts counting tiles 
    #from the bottom left corner, left to right, bottom to top, whereas the matrices 
    #require tuples (e.g. "2,3") and count top to bottom. Thus, the function assigns the 
    #proper row of the tuple according to the location of the Bitboard tile. For example
    #Bitboard tile 0 is A1 (the bottom left corner) while the appropriate matrix location 
    #is matrix[7,0].
    def tupler(tile):
        x = 0
        if tile < 8:
            x = 7
        elif 7 < tile < 16:
            x = 6
        elif 15 < tile < 24:
          x = 5
        elif 23 < tile < 32:
          x = 4
        elif 31 < tile < 40:
          x = 3
        elif 39 < tile < 48:
          x = 2
        elif 47 < tile < 56:
          x = 1
        elif 55 < tile < 64:
           x = 0
        return x,(tile % 8)
        #Iterate White's attacking influence
        for tile in range(64):
            winf[tupler(tile)] = len(bitboard.attackers(white, tile))
            
        print("\n")
        #Iterate Black's attacking influence        
        for tile in range(64):
            binf[tupler(tile)] = len(bitboard.attackers(black, tile))
            
        #Returns an array containing the white influence and black influence matrices    
        return [winf, binf]
            
    gameStart = makeInfluenceMatrices(chess.Bitboard())
    nextTurn = makeInfluenceMatrices(node.readBoard())
    x = 0
    for color in ["White","Black"]:
        print("{} Influence Matrix:\n{}".format(color, gameStart[x]))
        x += 1
        
    for color in ["White","Black"]:
        print("{} Influence Matrix:\n{}".format(color, nextTurn[x]))
        x += 1


    

#def makeInfluenceMatrices():
#    
#    ## Assigns the initial turn number to reference turn
#    turn = 0
#
#    ## Assigns a new game of chess, using the moves found in the file at reference pgn, to reference node
#    node = chess.pgn.read_game(pgn)
#
#    ## While there are turns remaining
#    while node.variations:
#
#        board = drawChessboard(512)
#        draw = ImageDraw.Draw(board)
#
#        ## Take one turn
#        node.board().san(node.variation (0).move)
#
#        squareNum = 0
#
#        ## For each square on the board
#        for key in squares:
#
#            ## Evaluate the number of attackers and adjust the list influence at index squareNum
#            influence [squareNum] += len(node.board().attackers (white,key))
#            squareNum += 1 
#
##        for key in influence:
##            draw.rectangle(xy=squares[key],fill='red')
#
#        ## Saves an image of the board
#        board.save("turn " + str(turn) + ".png")
#
#        ## Appends list turns with the saved image
#        turn.append("turn " + str(turn) + ".png")
#
#        ## Not entirely positive, something about resetting the turn
#        node = node.variation (0)
#
#        turn += 1
#
#        
## Other comments:

## This function opens the image stored at reference im
## Might be useful just so we can see what we're doing as we add in the chess pieces and shading
#   im.show()

## To call the getInfluence function you just put in the color and number of pixels for the parameters
## for instance, getInfluence(white, 500)

## Right now the background color when the image is created is black
## This will have to be changed to gray, I'll figure out how to do that and change the code

## The infShade function will use the PIL library and the coordinates used in drawChessboard to color in influence




def drawChessboard(color, bitboard):

    ## Assigns a new image to reference im with side length 512
    im = Image.new('L',(512,512),255)

    ## Assigns the PIL draw function to reference draw, for the image stored at reference im 
    draw = ImageDraw.Draw(im)

    ## Draw gray squares at every other coordinate in the list
    for i,k in zip(rows1357[0::2],rows1357[1::2]):
        draw.rectangle(xy=i,fill='gray')
    for i,k in zip(rows2468[0::2],rows2468[1::2]):
        draw.rectangle(xy=k,fill='gray')

#    for pieces in bitboard:
#        draw pieces

#    for square in squares:
#        shadeInfluence(color)

    return im
