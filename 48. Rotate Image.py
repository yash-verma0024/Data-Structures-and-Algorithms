from typing import List

##########################################################
#                Brute Force Solution                    #
##########################################################

# def rotate(matrix: List[List[int]]) -> None:
#     """
#     Do not return anything, modify matrix in-place instead.
#     """
#     n = len(matrix)
#     result = [[0 for i in range(n)] for _ in range(n)]
#     for i in range(0,n):
#         for j in range(0,n):
#             result[j][(n-1) -i] = matrix[i][j]
#     return result

# TC : O(N^2)
# SC : O(N^2)


##########################################################
#                  Optimal Solution                      #
##########################################################

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(0, n-1):
        for j in range(i+1, n):
            matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

    for i in range(0,n):
        matrix[i].reverse()
    return matrix

# TC : O(N*N) + O(N*N)  ~ O(N^2)
# SC : O(1)