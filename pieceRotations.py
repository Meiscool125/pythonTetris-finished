def moveBlockRight(currentBlock,grid,placedPieces):
    for piece in currentBlock.pieces:
        currentPieceRow = piece[0]
        currentPieceCol = piece[1]
        if currentPieceCol > 8:
            return currentBlock
        for square in placedPieces:
            placedSquareRow = square[0]
            placedSquareCol = square[1]
            if placedSquareRow == currentPieceRow:
                if placedSquareCol == currentPieceCol+1:
                    return currentBlock
    currentBlock.clear(grid)
    currentBlock.anchorCol += 1
    for piece in currentBlock.pieces:
        piece[1] += 1
    return currentBlock

def moveBlockLeft(currentBlock,grid,placedPieces):
    for piece in currentBlock.pieces:
        currentPieceRow = piece[0]
        currentPieceCol = piece[1]
        if currentPieceCol < 1:
            return currentBlock
        for square in placedPieces:
            placedSquareRow = square[0]
            placedSquareCol = square[1]
            if placedSquareRow == currentPieceRow:
                if placedSquareCol == currentPieceCol-1:
                    return currentBlock
    currentBlock.clear(grid)
    currentBlock.anchorCol -= 1
    for piece in currentBlock.pieces:
        piece[1] -= 1
    return currentBlock

def checkRotationBoundries(currentBlock):
    for piece in currentBlock.pieces:
        currentPieceRow = piece[0]
        currentPieceCol = piece[1]
        if currentPieceCol < 1:
            for part in currentBlock.pieces:
                part[1] += 1
        if currentPieceCol > 19:
            for part in currentBlock.pieces:
                part[1] -= 1

def rotatePiece(currentBlock, grid):
    currentBlock.clear(grid)
    if currentBlock.blockType == "O":
        pass
    if currentBlock.blockType == "I":
        if currentBlock.rotation == 0 or currentBlock.rotation == 180:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],
                [currentBlock.anchorRow-1, currentBlock.anchorCol],
                [currentBlock.anchorRow-2, currentBlock.anchorCol],
                [currentBlock.anchorRow+1, currentBlock.anchorCol]
            ]
            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 90 or currentBlock.rotation == 270:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],
                [currentBlock.anchorRow, currentBlock.anchorCol-1],
                [currentBlock.anchorRow, currentBlock.anchorCol-2],
                [currentBlock.anchorRow, currentBlock.anchorCol+1]
            ]
            checkRotationBoundries(currentBlock)
        checkRotationBoundries(currentBlock)
    if currentBlock.blockType == "T":
        if currentBlock.rotation == 0:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol], #anchor block (middle top)
                [currentBlock.anchorRow+1, currentBlock.anchorCol], #top right start       ---
                [currentBlock.anchorRow-1, currentBlock.anchorCol], #top left start        -
                [currentBlock.anchorRow, currentBlock.anchorCol+1] # bottom block start
            ]

            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 90:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol], #anchor block (middle top)
                [currentBlock.anchorRow, currentBlock.anchorCol+1], #top right start       ---
                [currentBlock.anchorRow, currentBlock.anchorCol-1], #top left start        -
                [currentBlock.anchorRow-1, currentBlock.anchorCol] # bottom block start
            ]
            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 180:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol], #anchor block (middle top)
                [currentBlock.anchorRow-1, currentBlock.anchorCol], #top right start       ---
                [currentBlock.anchorRow+1, currentBlock.anchorCol], #top left start        -
                [currentBlock.anchorRow, currentBlock.anchorCol-1] # bottom block start
            ]
            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 270:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol], #anchor block (middle top)
                [currentBlock.anchorRow, currentBlock.anchorCol+1], #top right start       ---
                [currentBlock.anchorRow, currentBlock.anchorCol-1], #top left start        -
                [currentBlock.anchorRow+1, currentBlock.anchorCol] # bottom block start
            ]
            checkRotationBoundries(currentBlock)

        checkRotationBoundries(currentBlock)
    if currentBlock.blockType == "J":
        if currentBlock.rotation == 0:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor block (middle top)
                [currentBlock.anchorRow-1, currentBlock.anchorCol],  # top right start       ---
                [currentBlock.anchorRow+1, currentBlock.anchorCol],  # top left start        -
                [currentBlock.anchorRow+1, currentBlock.anchorCol-1]  # bottom block start
            ]

            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 90:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor block (middle top)
                [currentBlock.anchorRow, currentBlock.anchorCol+1],  # top right start       ---
                [currentBlock.anchorRow, currentBlock.anchorCol-1],  # top left start        -
                [currentBlock.anchorRow-1, currentBlock.anchorCol-1]  # bottom block start
            ]
            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 180:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor block (middle top)
                [currentBlock.anchorRow-1, currentBlock.anchorCol],  # top right start       ---
                [currentBlock.anchorRow+1, currentBlock.anchorCol],  # top left start        -
                [currentBlock.anchorRow-1, currentBlock.anchorCol+1]  # bottom block start
            ]
            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 270:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor block (middle top)
                [currentBlock.anchorRow, currentBlock.anchorCol+1],  # top right start       ---
                [currentBlock.anchorRow, currentBlock.anchorCol-1],  # top left start        -
                [currentBlock.anchorRow+1, currentBlock.anchorCol+1]  # bottom block start
            ]
            checkRotationBoundries(currentBlock)

        checkRotationBoundries(currentBlock)
    if currentBlock.blockType == "L":
        if currentBlock.rotation == 0:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor block (middle top)
                [currentBlock.anchorRow+1, currentBlock.anchorCol],  # top right start       ---
                [currentBlock.anchorRow-1, currentBlock.anchorCol],  # top left start        -
                [currentBlock.anchorRow-1, currentBlock.anchorCol-1]  # bottom block start
            ]

            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 90:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor block (middle top)
                [currentBlock.anchorRow, currentBlock.anchorCol-1],  # top right start       ---
                [currentBlock.anchorRow, currentBlock.anchorCol+1],  # top left start        -
                [currentBlock.anchorRow-1, currentBlock.anchorCol+1]  # bottom block start
            ]
            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 180:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor block (middle top)
                [currentBlock.anchorRow+1, currentBlock.anchorCol],  # top right start       ---
                [currentBlock.anchorRow-1, currentBlock.anchorCol],  # top left start        -
                [currentBlock.anchorRow+1, currentBlock.anchorCol+1]  # bottom block start
            ]
            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 270:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor block (middle top)
                [currentBlock.anchorRow, currentBlock.anchorCol-1],  # top right start       ---
                [currentBlock.anchorRow, currentBlock.anchorCol+1],  # top left start        -
                [currentBlock.anchorRow+1, currentBlock.anchorCol-1]  # bottom block start
            ]
            checkRotationBoundries(currentBlock)

        checkRotationBoundries(currentBlock)
    if currentBlock.blockType == "Z":
        if currentBlock.rotation == 0 or currentBlock.rotation == 180:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor block (middle top)
                [currentBlock.anchorRow+1, currentBlock.anchorCol],  # top right start       ---
                [currentBlock.anchorRow, currentBlock.anchorCol+1],  # top left start        -
                [currentBlock.anchorRow-1, currentBlock.anchorCol+1]  # bottom block start
            ]

            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 90 or currentBlock.rotation == 270:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor of Z block is top right square
                [currentBlock.anchorRow + 1, currentBlock.anchorCol],
                [currentBlock.anchorRow, currentBlock.anchorCol - 1],
                [currentBlock.anchorRow + 1, currentBlock.anchorCol + 1]
            ]
            checkRotationBoundries(currentBlock)

    if currentBlock.blockType == "S":
        if currentBlock.rotation == 0 or currentBlock.rotation == 180:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor block (middle top)
                [currentBlock.anchorRow -1, currentBlock.anchorCol],  # top right start       ---
                [currentBlock.anchorRow, currentBlock.anchorCol + 1],  # top left start        -
                [currentBlock.anchorRow + 1, currentBlock.anchorCol + 1]  # bottom block start
            ]

            checkRotationBoundries(currentBlock)
        if currentBlock.rotation == 90 or currentBlock.rotation == 270:
            currentBlock.pieces = [
                [currentBlock.anchorRow, currentBlock.anchorCol],  # anchor of S block is top left square
                [currentBlock.anchorRow, currentBlock.anchorCol + 1],
                [currentBlock.anchorRow + 1, currentBlock.anchorCol],
                [currentBlock.anchorRow + 1, currentBlock.anchorCol - 1]
            ]
            checkRotationBoundries(currentBlock)
        checkRotationBoundries(currentBlock)
    currentBlock.rotation += 90
    if currentBlock.rotation == 360:
        currentBlock.rotation = 0


