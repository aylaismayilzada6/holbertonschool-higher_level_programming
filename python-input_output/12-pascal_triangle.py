#!/usr/bin/python3
"""Module that generates Pascal's triangle"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of size n"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        # start each row with 1
        row = [1] * (i + 1)
        # Calculate middle values
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
