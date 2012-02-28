#!/usr/bin/env python

from Scimitar import *
import numpy as np

def l2normShouldReturnZeroForZeroVector():
   testvect = np.zeros(100)
   assert(0 == l2norm(testvect))

def l2normShouldReturnNForOnes():
   testvect = ones(100)
   assert(100 == l2norm(testvect))

def l2normShouldReturnCorrectl2NormWithNegativeValues():
   testvect = array([-2,2,-2,2])
   assert(16 == l2norm(testvect))

def main():
   l2normShouldReturnZeroForZeroVector()

if __name__ == "__main__":
   main()

def TestCondition(cond, line):
   if not cond:
      print "Failed Assert on line %d!" % (line,)
