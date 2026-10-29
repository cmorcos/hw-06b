
# -*- coding: utf-8 -*-
"""
Triangle classification program.
"""

def classifyTriangle(a, b, c):
    """
    Classifies a triangle based on its three sides.
    """

    # Check that inputs are integers
    if not (isinstance(a, int) and
            isinstance(b, int) and
            isinstance(c, int)):
        return 'InvalidInput'

    # Check that sides are between 1 and 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # fix 1: changed b <= b to b <= 0
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # fix 2 --> correct triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'

    # fix 3 --> check all three sides
    if a == b and b == c:
        return 'Equilateral'

    # fix 4 --> use pythagorean theorem
    elif (a**2 + b**2 == c**2 or
          a**2 + c**2 == b**2 or
          b**2 + c**2 == a**2):
        return 'Right'

    # fix 5 --> compare all three pairs
    elif a != b and b != c and a != c:
        return 'Scalene'

    else:
        return 'Isoceles'
