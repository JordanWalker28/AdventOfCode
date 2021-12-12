from functions import *

lines = readTextFile("input/day3-1.txt")

bits = createBits(lines)
data = createDataShape(lines)

print(calculateEpsilonTimesGamma(data, bits))
print(calculateLifeSupport(data, bits))