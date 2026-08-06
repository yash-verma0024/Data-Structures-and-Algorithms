##########################################################
#                Brute Force Solution                    #
##########################################################

from typing import List

def markinfinite(matrix, row, col):
    r,c = len(matrix) , len(matrix[0])
    for i in range(0,r):
        if matrix[i][col] != 0:
            matrix[i][col] = float("inf")

    for j in range(0,c):
        if matrix[row][j] != 0:
            matrix[row][j] = float("inf")

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    r,c = len(matrix) , len(matrix[0])
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == 0:
                markinfinite(matrix, i, j)

    for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0
    return matrix


# TC : O((N+M) * (N*M)) + O(N*M)
# SC : O(1)

##########################################################
#                  Optimal Solution                      #
##########################################################


def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    row_track = [0 for _ in range(rows)]
    col_track = [0 for _ in range(cols)]

    for i in range(0, rows):
          for j in range(0, cols):
                if matrix[i][j] == 0:
                      row_track[i] = -1 
                      col_track[j] = -1
    for i in range(0, rows):
        for j in range(0, cols):
            if row_track[i] == -1 or col_track[j] == -1:
                matrix[i][j] = 0
    return matrix

# TC : (2 X (N*M)) ~ (N*M)
# SC : O(rows * COLS)