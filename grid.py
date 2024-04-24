import pygame

# base grid is 300x600
def makeGrid(width, height):
    grid = []
    cellWidth = 30
    cellHeight = 30
    for i in range(20):
        grid.append([[0, (255,255,255)] for j in range(10)])
    return grid



"""
grid = [[[0],[0],[0],0,0,0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,[1],[1],0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,[1],[1],0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,[2, [255, 255, 255]],2,0,0,0,0,],
        [0,0,0,0,0,0,0,0,2,2,0,0,0,0,],]

grid[4][8][1]
"""