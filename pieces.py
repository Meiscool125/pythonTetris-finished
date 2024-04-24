import pygame
from grid import *
import random

# a BLOCK is the end shape
# a SQUARE is the 4 squares the BLOCK is made of
# the ANCHOR SQUARE is the main rotation point of the BLOCK
# the ANCHOR SQUARE should always be index zero of the list

# pices as imgs
OBlockImg = pygame.image.load('imgs/O Block.png')
IBlockImg = pygame.image.load('imgs/I Block.png')
TBlockImg = pygame.image.load('imgs/T Block.png')
JBlockImg = pygame.image.load('imgs/J Block.png')
LBlockImg = pygame.image.load('imgs/L Block.png')
ZBlockImg = pygame.image.load('imgs/Z Block.png')
SBlockImg = pygame.image.load('imgs/S Block.png')

blockTypes = ["O","I","T","J","L","Z","S"]

nextBlock = [random.choice(blockTypes)]
# nextBlock = I
# currentBlock = I
# NextBlock = T
# currentBlock = T
def makeBlock():
    randomBlock = random.choice(blockTypes)
    list.append(nextBlock, randomBlock)
    try:
        currentBlock = Block(0,3,nextBlock[0]) # should be nextBlock[0] for random block
        list.pop(nextBlock, 0)
        #currentBlock = Block(0,3,randomBlock) #change to a block of your choice surrounded by "" to make it always that block. (i.e "I"). change back to randomBlock to make it normal again
        return currentBlock
    except Exception as exception:
        print(f'Error: {exception}')
        currentBlock = Block(0, 3, randomBlock)
        return currentBlock
#def showNextBlock():

def makeFirstBlock():
    randomBlock = random.choice(blockTypes)
    currentBlock = Block(0,3,randomBlock) #change to a block of your choice surrounded by "" to make it always that block. (i.e "I"). change back to randomBlock to make it normal again
    return currentBlock

def moveBlockDown(currentBlock, grid):
    currentBlock.clear(grid)
    currentBlock.anchorRow += 1
    for piece in currentBlock.pieces:
        piece[0] += 1

def getNextPieceImage(nextBlock):
    # returns the pygame surface that we want to blit onto the screen. In other words returns the image of the block
    if nextBlock == ['O']:
        return OBlockImg
    if nextBlock == ['I']:
        return IBlockImg
    if nextBlock == ['T']:
        return TBlockImg
    if nextBlock == ['J']:
        return JBlockImg
    if nextBlock == ['L']:
        return LBlockImg
    if nextBlock == ['Z']:
        return ZBlockImg
    if nextBlock == ['S']:
        return SBlockImg
class Block:
    def __init__(self,anchorRow,anchorCol,blockType):
        self.anchorRow = anchorRow
        self.anchorCol = anchorCol
        self.blockType = blockType
        self.blocks = []
        self.color = None
        self.rotation = 0
        self.setup()
    def setup(self):
        if self.blockType == "O": #that is an O not a zero
            self.pieces = [
                           [self.anchorRow, self.anchorCol], #anchor of O block is top left square
                           [self.anchorRow, self.anchorCol + 1],
                           [self.anchorRow + 1, self.anchorCol],
                           [self.anchorRow + 1, self.anchorCol + 1]
                           ]
            self.color = (0, 0, 255)  # blue
        elif self.blockType == "I":
            self.anchorCol +=1
            self.pieces = [
                           [self.anchorRow, self.anchorCol], #anchor of I block is 3rd square (counting left -> right)
                           [self.anchorRow, self.anchorCol+1],
                           [self.anchorRow, self.anchorCol-1],
                           [self.anchorRow, self.anchorCol-2]
                            ]
            self.color = (100,100,0) # yellow
        elif self.blockType == "T":
            self.pieces = [
                           [self.anchorRow, self.anchorCol], #anchor of T block is middle of line of 3
                           [self.anchorRow, self.anchorCol+1],
                           [self.anchorRow, self.anchorCol-1],
                           [self.anchorRow+1, self.anchorCol]
                            ]
            self.color = (0,255,0) # green
        elif self.blockType == "J":
            self.pieces = [
                           [self.anchorRow, self.anchorCol], #anchor of J block is middle of line of 3
                           [self.anchorRow, self.anchorCol+1],
                           [self.anchorRow, self.anchorCol-1],
                           [self.anchorRow+1, self.anchorCol+1]
                            ]
            self.color = (0,100,100) # cyan
        elif self.blockType == "L":
            self.pieces = [
                           [self.anchorRow, self.anchorCol], #anchor of L block is middle of line of 3
                           [self.anchorRow, self.anchorCol+1],
                           [self.anchorRow, self.anchorCol-1],
                           [self.anchorRow+1, self.anchorCol-1]
                            ]
            self.color = (100,0,100) # purple guy (fnaf reference)
        elif self.blockType == "Z":
            self.pieces = [
                           [self.anchorRow, self.anchorCol], #anchor of Z block is top right square
                           [self.anchorRow+1, self.anchorCol],
                           [self.anchorRow, self.anchorCol-1],
                           [self.anchorRow+1, self.anchorCol+1]
                            ]
            self.color = (150,0,75) # brown (like freddy forgbear)
        elif self.blockType == "S":
            self.pieces = [
                           [self.anchorRow, self.anchorCol], #anchor of S block is top left square
                           [self.anchorRow, self.anchorCol+1],
                           [self.anchorRow+1, self.anchorCol],
                           [self.anchorRow+1, self.anchorCol-1]
                            ]
            self.color = (255,127,80) # coral (like foxy)

    def clear(self, grid):
        for piece in self.pieces:
            grid[piece[0]][piece[1]] = [0, (255,255,255)]



