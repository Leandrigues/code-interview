# DailyCoding 14
import numpy as np
import random

def generatePoints(n = 500):
  circlePoints = squarePoints = 0

  for iteration in range(n):
    i = random.uniform(-1, 1)
    j = random.uniform(-1, 1)
    if i**2 + j**2 <= 1:
      circlePoints += 1
    squarePoints += 1

  return (squarePoints, circlePoints)

def monteCarlo():
  squarePoints, circlePoints = generatePoints(10**6)
  piEstimation = 4 * circlePoints / squarePoints
  print(piEstimation)

monteCarlo()