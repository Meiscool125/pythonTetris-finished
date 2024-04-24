import pygame
import time
import random


# pygame.init starts the code
pygame.init()

# get other files
from grid import *
from pieces import *
from pieceRotations import *

# create time
clock = pygame.time.Clock()

# fonts
mainFont = pygame.font.Font(None, 46)
smallFont = pygame.font.Font(None, 35)

# set variable that is true
CurrentlyRunning = True

#toggle
toggle = True

# screen setup
screen = pygame.display.set_mode((700, 700))

# make bg color incase img fails to load
screen.fill((0, 0, 0))

# make the name of the window
pygame.display.set_caption('Python Tetris')
scene = None

placedPieces = []
placedPiecesColors = []
colorIndex = 0
piecesPlaced = -1

currentBlock = makeFirstBlock()
#(currentBlock.pieces)

grid = makeGrid(300,600)
score = 0
def blitText(text: object, font: object, color: object, pos: object, screen: object) -> object:
    textToBlit = font.render(text,True,color)
    screen.blit(textToBlit, pos)

def drawEdges():
    pygame.draw.rect(screen, (255,255,255), (400,55,2,120))
    pygame.draw.rect(screen, (255, 255, 255), (400, 55, 250, 2))
    pygame.draw.rect(screen, (255,255,255), (400,175,250,2))
    pygame.draw.rect(screen, (255,255,255), (650,55,2,120))

def drawGrid(currentBlock):
    for piece in currentBlock.pieces:
        pieceRow = piece[0]
        pieceCol = piece[1]
        #print("pieceRow:", pieceRow, "pieceCol:", pieceCol)
        grid[pieceRow][pieceCol] = [1, currentBlock.color]

    #placedPieces = [[2,3],[2,4],[2,5],[2,6]]
    #placedPiecesColors = [[255,0,0],[255,0,0],[255,0,0],[255,0,0]]
    for index, square in enumerate(placedPieces):
        pieceRow = square[0]
        pieceCol = square[1]
        #print("placed square[0]:", square[0])
        grid[pieceRow][pieceCol] = [2, placedPiecesColors[index]]

    #cell dimensions
    cellWidth = 30
    cellHeight = 30
    offsetx = offsety = 50 + 10

    pygame.draw.rect(screen, (255,255,255), (55, 55, 305, 605), 5)
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if grid[y][x][0] == 0: # drawimg white BG
                pygame.draw.rect(screen, (255,255,255), (offsetx+x*cellWidth, offsety+y*cellHeight, cellWidth-2,cellHeight-2))
            elif grid[y][x][0] == 1: # drawing the current Block
                pygame.draw.rect(screen, currentBlock.color,
                                 (offsetx + x * cellWidth, offsety + y * cellHeight, cellWidth - 2, cellHeight - 2))
            elif grid[y][x][0] == 2: # drawing placed pieces
                pygame.draw.rect(screen, grid[y][x][1],
                                 (offsetx + x * cellWidth, offsety + y * cellHeight, cellWidth - 2, cellHeight - 2))

def checkForFullRow(currentBlock):
    global grid
    global score
    spotsFilled = 0
    for piece in currentBlock.pieces:
        grid[piece[0]][piece[1]] = [0, [255,255,255]]
    for y, row in enumerate(grid):
        spotsFilled = 0
        for x, col in enumerate(row):
            if grid[y][x][0] != 0:
                spotsFilled +=1
            else:
                break
        if spotsFilled == 10:
            #print("row filled")
            blockToRemove = []
            colorIndexesToRemove = []
            for index, piece in enumerate(placedPieces):
                if piece[0] == y:
                    blockToRemove.append(piece)
                    colorIndexesToRemove.append(index)

            blockToRemove.reverse()
            colorIndexesToRemove.reverse()
            for block in blockToRemove:
                placedPieces.remove(block)
            for index in colorIndexesToRemove:
                placedPiecesColors.pop(index)
            grid = makeGrid(300, 600)
            for i in range(len(placedPieces)):
                if placedPieces[i][0] < y:
                    placedPieces[i][0] += 1
            score += 100
startTime = pygame.time.get_ticks()/1000
currentTime = pygame.time.get_ticks()/1000 - startTime
timeSinceLastBlockMovement = currentTime
timeSinceLastBlockMade = currentTime

while CurrentlyRunning:
    checkForFullRow(currentBlock)
    currentTime = pygame.time.get_ticks() / 1000 - startTime
    screen.fill((0,0,0))
    drawEdges()
    blitText('Next:', smallFont, (255,255,255), (485,70), screen)
    if scene == None:
        pass #change to main menu at later date maybe?

    for event in pygame.event.get():
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the mouse position
            x, y = pygame.mouse.get_pos()
            print("Mouse clicked at ({}, {})".format(x, y))
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                currentBlock = moveBlockRight(currentBlock,grid,placedPieces)
            if event.key == pygame.K_LEFT:
                currentBlock = moveBlockLeft(currentBlock,grid,placedPieces)
            if event.key ==  pygame.K_DOWN:
                moveBlockDown(currentBlock,grid)
            if event.key == pygame.K_UP:
                rotatePiece(currentBlock, grid)
        if event.type == pygame.QUIT:
            # user clicked close button
            CurrentlyRunning = False
    if currentTime - timeSinceLastBlockMovement >= 0.3  and shouldPlaceBlock == False: #default timeSinceLastBlockMovement is 0.3 (controls falling speed)
        moveBlockDown(currentBlock, grid)
        timeSinceLastBlockMovement = currentTime

    if toggle == True:
        pass
    if toggle == False:
        #print("nextBlock", nextBlock)
        screen.blit(getNextPieceImage(nextBlock), (470, 100))

    shouldPlaceBlock = False
    for piece in currentBlock.pieces:
        if piece[0] > 18:
            shouldPlaceBlock = True
            continue
    for currentPiece in currentBlock.pieces:
        currentPieceRow = currentPiece[0]
        currentPieceCol = currentPiece[1]
        for square in placedPieces:
            placedSquareRow = square[0]
            placedSquareCol = square[1]
            if currentPieceRow+1 == placedSquareRow:
                if currentPieceCol == placedSquareCol:
                    shouldPlaceBlock = True

    if shouldPlaceBlock:
        piecesPlaced += 1
        for i in range(len(currentBlock.pieces)):
            placedPieces.append(currentBlock.pieces[i])
            placedPiecesColors.append(currentBlock.color)
        #("placedPieces:", placedPieces)
        #print("placedPiecesColors:", placedPiecesColors)

        if (currentTime - timeSinceLastBlockMade) < 0.2: #if we hit the top of the screen
            CurrentlyRunning = False
            if piecesPlaced >= 2147483647:
                urBadGetGood = 'cheater'
                piecesPlaced = 'more than the goddamn integer limit holy cannoli'
            else:
                urBadGetGood = 'ur bad kid get good'
            print(f'----------------------------\n {urBadGetGood}\n number of pieces placed: {piecesPlaced}\n----------------------------')
            print(f'Score: {score}')

        else:
            currentBlock = makeBlock()
            timeSinceLastBlockMade = currentTime
    blitText((f'Score: {score}'), smallFont, (255,255,255), (400,200), screen)

    drawGrid(currentBlock)
    toggle = False
    # limit the frame rate
    clock.tick(60)
    # update the display
    pygame.display.flip()

pygame.quit()


