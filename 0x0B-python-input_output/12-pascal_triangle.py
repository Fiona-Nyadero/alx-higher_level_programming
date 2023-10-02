#!/usr/bin/python3
"""defines a pascal_triangle module."""


def pascal_triangle(n):
    """reps a pascal triangle class"""

    if n <= 0:
        return []

    triangle = []
    for y in range(n):
        rw = [1]
        if y > 0:
            prev_row = triangle[y - 1]
            for k in range(1, y):
                rw.append(prev_row[k - 1] + prev_row[k])
            rw.append(1)  # Last element is always 1
        triangle.append(rw)

    return triangle
