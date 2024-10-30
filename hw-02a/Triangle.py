# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(a, b, c):
    """
    Classify a triangle based on the lengths of its sides.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the triangle.

    Returns:
        'Equilateral' if all three sides are equal
        'Isosceles' if exactly one pair of sides are equal
        'Scalene' if no pair of sides are equal
        'NotATriangle' if the lengths cannot form a triangle
        'Right' if the triangle is a right triangle

    Validations:
        - Input values must be integers between 1 and 200 (inclusive)
    """

    # Require that the input values be >= 1 and <= 200
    if not (1 <= a <= 200 and 1 <= b <= 200 and 1 <= c <= 200):
        return 'InvalidInput'

    # Verify that all 3 inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # Check for the triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Now we know that we have a valid triangle
    if a == b == c:
        return 'Equilateral'

    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        return 'Right'

    if a == b or b == c or a == c:
        return 'Isosceles'

    return 'Scalene'
