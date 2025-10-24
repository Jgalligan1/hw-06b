# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(3,3,3), 'Equilateral')
        self.assertEqual(classifyTriangle(200,200,200), 'Equilateral')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(5,5,8), 'Isosceles')
        self.assertEqual(classifyTriangle(8,5,5), 'Isosceles')
        self.assertEqual(classifyTriangle(5,8,5), 'Isosceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(4,5,6), 'Scalene')

    def testRightTriangles(self):
        self.assertEqual(classifyTriangle(3,4,5), 'Right')
        self.assertEqual(classifyTriangle(5,3,4), 'Right')
        self.assertEqual(classifyTriangle(5,12,13), 'Right')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,1,3), 'NotATriangle')
        self.assertEqual(classifyTriangle(1,10,12), 'NotATriangle')

    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(0,4,5), 'InvalidInput')
        self.assertEqual(classifyTriangle(-1,4,5), 'InvalidInput')
        self.assertEqual(classifyTriangle(201,100,100), 'InvalidInput')
        self.assertEqual(classifyTriangle('a',3,5), 'InvalidInput')
        self.assertEqual(classifyTriangle(3,3.5,3), 'InvalidInput')

if __name__ == '__main__':
    unittest.main()
