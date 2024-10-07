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
    # Right triangles
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    # Equilateral triangles
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    # Isosceles triangles
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2,2,3 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isosceles', '3,2,2 should be isosceles')

    # Scalene triangles
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(4, 6, 9), 'Scalene', '4,6,9 should be scalene')

    # Invalid triangles
    def testInvalidTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a valid triangle')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'NotATriangle', '0,1,1 is not a valid triangle')

    def testInvalidTriangleC(self):
        self.assertEqual(classifyTriangle(-1, 1, 2), 'NotATriangle', '-1,1,2 is not a valid triangle')

    # Floating point precision
    def testFloatingPointTriangle(self):
        self.assertEqual(classifyTriangle(0.3, 0.4, 0.5), 'Right', '0.3,0.4,0.5 should be a Right triangle')

if __name__ == '__main__':
    unittest.main()