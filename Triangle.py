# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Oct 2025

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@updated_by: Jack Galligan
"""

def classifyTriangle(a, b, c):
    """
    Classify a triangle based on the lengths of its three sides.
    """

    # ----- Input validation -----
    # All sides must be integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # All sides must be within 0 < side <= 200
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # ----- Triangle inequality check -----
    # The sum of any two sides must be greater than the third
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # ----- Right triangle check -----
    sides = sorted([a, b, c])  # sort to make sure hypotenuse is last
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'Right'

    # ----- Equilateral / Isosceles / Scalene -----
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'
