#!/usr/bin/python3
"""rotate 2d matrix module"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix 90 degrees clockwise"""
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = tmp
