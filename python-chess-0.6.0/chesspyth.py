from __future__ import print_function
import chess.pgn
from PIL import Image, ImageDraw

whiteInfluence = []
blackInfluence = []

whiteInfluenceImage = []
blackInfluenceImage = []

## Assigns a new image to reference im with side length 512
white = Image.new('RGB',(512,512),'white')
black = Image.new('RGB',(512,512),'white')

## Assigns the PIL draw function to reference draw, for the image stored at reference im
draw = ImageDraw.Draw(white)
draw2 = ImageDraw.Draw(black)
## Assigns an empty list to reference turn. This will be used to store the bitboard for each turn in the game.
turn = []

## Length in pixels of one side of one square.
s = 64

## These are most likely not the lists of data we will end up with when the program is finished, they can be updated as we continue writing
## the code and figure out what type of data we need and in what format.
coords = [[(s*0,s*0),(s*1,s*1)], [(s*1,s*0),(s*2,s*1)], [(s*2,s*0),(s*3,s*1)], [(s*3,s*0),(s*4,s*1)], [(s*4,s*0),(s*5,s*1)], [(s*5,s*0),(s*6,s*1)], [(s*6,s*0),(s*7,s*1)], [(s*7,s*0),(s*8,s*1)],
          [(s*0,s*1),(s*1,s*2)], [(s*1,s*1),(s*2,s*2)], [(s*2,s*1),(s*3,s*2)], [(s*3,s*1),(s*4,s*2)], [(s*4,s*1),(s*5,s*2)], [(s*5,s*1),(s*6,s*2)], [(s*6,s*1),(s*7,s*2)], [(s*7,s*1),(s*8,s*2)],
          [(s*0,s*2),(s*1,s*3)], [(s*1,s*2),(s*2,s*3)], [(s*2,s*2),(s*3,s*3)], [(s*3,s*2),(s*4,s*3)], [(s*4,s*2),(s*5,s*3)], [(s*5,s*2),(s*6,s*3)], [(s*6,s*2),(s*7,s*3)], [(s*7,s*2),(s*8,s*3)],
          [(s*0,s*3),(s*1,s*4)], [(s*1,s*3),(s*2,s*4)], [(s*2,s*3),(s*3,s*4)], [(s*3,s*3),(s*4,s*4)], [(s*4,s*3),(s*5,s*4)], [(s*5,s*3),(s*6,s*4)], [(s*6,s*3),(s*7,s*4)], [(s*7,s*3),(s*8,s*4)],
          [(s*0,s*4),(s*1,s*5)], [(s*1,s*4),(s*2,s*5)], [(s*2,s*4),(s*3,s*5)], [(s*3,s*4),(s*4,s*5)], [(s*4,s*4),(s*5,s*5)], [(s*5,s*4),(s*6,s*5)], [(s*6,s*4),(s*7,s*5)], [(s*7,s*4),(s*8,s*5)],
          [(s*0,s*5),(s*1,s*6)], [(s*1,s*5),(s*2,s*6)], [(s*2,s*5),(s*3,s*6)], [(s*3,s*5),(s*4,s*6)], [(s*4,s*5),(s*5,s*6)], [(s*5,s*5),(s*6,s*6)], [(s*6,s*5),(s*7,s*6)], [(s*7,s*5),(s*8,s*6)],
          [(s*0,s*6),(s*1,s*7)], [(s*1,s*6),(s*2,s*7)], [(s*2,s*6),(s*3,s*7)], [(s*3,s*6),(s*4,s*6)], [(s*4,s*6),(s*5,s*7)], [(s*5,s*6),(s*6,s*7)], [(s*6,s*6),(s*7,s*7)], [(s*7,s*6),(s*8,s*7)],
          [(s*0,s*7),(s*1,s*8)], [(s*1,s*7),(s*2,s*8)], [(s*2,s*7),(s*3,s*8)], [(s*3,s*7),(s*4,s*8)], [(s*4,s*7),(s*5,s*8)], [(s*5,s*7),(s*6,s*8)], [(s*6,s*7),(s*7,s*8)], [(s*7,s*7),(s*8,s*8)]]
rows1357 = [[(s*0,s*7),(s*1,s*8)],[(s*1,s*7),(s*2,s*8)],[(s*2,s*7),(s*3,s*8)],[(s*3,s*7),(s*4,s*8)],[(s*4,s*7),(s*5,s*8)],[(s*5,s*7),(s*6,s*8)],[(s*6,s*7),(s*7,s*8)],[(s*7,s*7),(s*8,s*8)],
            [(s*0,s*5),(s*1,s*6)],[(s*1,s*5),(s*2,s*6)],[(s*2,s*5),(s*3,s*6)],[(s*3,s*5),(s*4,s*6)],[(s*4,s*5),(s*5,s*6)],[(s*5,s*5),(s*6,s*6)],[(s*6,s*5),(s*7,s*6)],[(s*7,s*5),(s*8,s*6)],
            [(s*0,s*3),(s*1,s*4)],[(s*1,s*3),(s*2,s*4)],[(s*2,s*3),(s*3,s*4)],[(s*3,s*3),(s*4,s*4)],[(s*4,s*3),(s*5,s*4)],[(s*5,s*3),(s*6,s*4)],[(s*6,s*3),(s*7,s*4)],[(s*7,s*3),(s*8,s*4)],
            [(s*0,s*1),(s*1,s*2)],[(s*1,s*1),(s*2,s*2)],[(s*2,s*1),(s*3,s*2)],[(s*3,s*1),(s*4,s*2)],[(s*4,s*1),(s*5,s*2)],[(s*5,s*1),(s*6,s*2)],[(s*6,s*1),(s*7,s*2)],[(s*7,s*1),(s*8,s*2)]]
rows2468 = [[(s*0,s*6),(s*1,s*7)],[(s*1,s*6),(s*2,s*7)],[(s*2,s*6),(s*3,s*7)],[(s*3,s*6),(s*4,s*7)],[(s*4,s*6),(s*5,s*7)],[(s*5,s*6),(s*6,s*7)],[(s*6,s*6),(s*7,s*7)],[(s*7,s*6),(s*8,s*7)],
            [(s*0,s*4),(s*1,s*5)],[(s*1,s*4),(s*2,s*5)],[(s*2,s*4),(s*3,s*5)],[(s*3,s*4),(s*4,s*5)],[(s*4,s*4),(s*5,s*5)],[(s*5,s*4),(s*6,s*5)],[(s*6,s*4),(s*7,s*5)],[(s*7,s*4),(s*8,s*5)],
            [(s*0,s*2),(s*1,s*3)],[(s*1,s*2),(s*2,s*3)],[(s*2,s*2),(s*3,s*3)],[(s*3,s*2),(s*4,s*3)],[(s*4,s*2),(s*5,s*3)],[(s*5,s*2),(s*6,s*3)],[(s*6,s*2),(s*7,s*3)],[(s*7,s*2),(s*8,s*3)],
            [(s*0,s*0),(s*1,s*1)],[(s*1,s*0),(s*2,s*1)],[(s*2,s*0),(s*3,s*1)],[(s*3,s*0),(s*4,s*1)],[(s*4,s*0),(s*5,s*1)],[(s*5,s*0),(s*6,s*1)],[(s*6,s*0),(s*7,s*1)],[(s*7,s*0),(s*8,s*1)]]
tiles = [chess.A8, chess.B8, chess.C8, chess.D8, chess.E8, chess.F8, chess.G8, chess.H8,
         chess.A7, chess.B7, chess.C7, chess.D7, chess.E7, chess.F7, chess.G7, chess.H7,
         chess.A6, chess.B6, chess.C6, chess.D6, chess.E6, chess.F6, chess.G6, chess.H6,
         chess.A5, chess.B5, chess.C5, chess.D5, chess.E5, chess.F5, chess.G5, chess.H5,
         chess.A4, chess.B4, chess.C4, chess.D4, chess.E4, chess.F4, chess.G4, chess.H4,
         chess.A3, chess.B3, chess.C3, chess.D3, chess.E3, chess.F3, chess.G3, chess.H3,
         chess.A2, chess.B2, chess.C2, chess.D2, chess.E2, chess.F2, chess.G2, chess.H2,
         chess.A1, chess.B1, chess.C1, chess.D1, chess.E1, chess.F1, chess.G1, chess.H1]

pgn = open ("CompGM.pgn")
node = chess.pgn.read_game(pgn)
turn.append(node.board())
while node.variations:
    node.board().san(node.variation (0).move)
    node = node.variation (0)
    turn.append(node.board())
pgn.close()


#The parameter of this function is the specified index of the list turn
def makeInfluenceMatrices(index):

    #Initialize each influence matrix, i.e 8x8 matrices of 0's
    winf = [0]*64
    binf = [0]*64

    #Iterate White's attacking influence
    for tile in tiles:
        winf[tile] = len(turn[index].attackers(chess.WHITE, tile))
    for tile in tiles:
        binf[tile] = len(turn[index].attackers(chess.BLACK, tile))

    whiteInfluence.append(winf)
    blackInfluence.append(binf)


def shadeInfluence(drawNum, influenceMatrix):

    i = 0

    for index in influenceMatrix:
        if index != 0:
            opacity = index * 30
            red = 255 - opacity, 0, 0
            drawNum.rectangle(xy = coords[i], fill = red)
        i += 1


#def drawPieces():


def drawBoard(turn):

    makeInfluenceMatrices(turn)

    ## Draw gray squares at every other coordinate in the list
    for i,k in zip(rows1357[0::2], rows1357[1::2]):
        draw.rectangle(xy = i,fill = 'gray')
    for i,k in zip(rows2468[0::2], rows2468[1::2]):
        draw.rectangle(xy = k,fill = 'gray')

    shadeInfluence(draw, whiteInfluence[turn])

    ## Draw gray squares at every other coordinate in the list
    for i,k in zip(rows1357[0::2], rows1357[1::2]):
        draw2.rectangle(xy = i,fill = 'gray')
    for i,k in zip(rows2468[0::2], rows2468[1::2]):
        draw2.rectangle(xy = k,fill = 'gray')


    shadeInfluence(draw2, blackInfluence[turn])

#    for pieces in bitboard:
#        draw pieces

    whiteInfluenceImage.append(white)
    blackInfluenceImage.append(black)