# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isoceles')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(5, 8, 5), 'Isoceles')

    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(8, 5, 5), 'Isoceles')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def testZeroSide(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'InvalidInput')

    def testNegativeSide(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), 'InvalidInput')

    def testAboveMaximum(self):
        self.assertEqual(classifyTriangle(201, 4, 5), 'InvalidInput')

    def testNonInteger(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

