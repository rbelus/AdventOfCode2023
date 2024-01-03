import regex
import os
import sys
import math
import functools
import operator

sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
input = open("input", "r")

numRegex = regex.compile(r"\d+")

line = input.readline()
timeList = [i for i in numRegex.findall(line)]
line = input.readline()
distList = [i for i in numRegex.findall(line)]


# simply solve polynomial to found bounds of winning holding time values
wayCode = []
for raceIndex in range(len(timeList)):
    y = int(distList[raceIndex])
    maxX = float(timeList[raceIndex])
    delta = float(maxX * maxX - 4 * y)
    x1 = (-maxX + math.sqrt(delta)) / -2.
    x2 = (-maxX - math.sqrt(delta)) / -2.

    if x1 == math.ceil(x1):
        x1 = x1 + 1.
    if x2 == math.floor(x2):
        x2 = x2 - 1.

    x1 = math.ceil(x1)
    x2 = math.floor(x2)

    wayCode.append(x2 - x1 + 1)

print("day6 part 1:", functools.reduce(operator.mul, wayCode))

bigMaxX = int(functools.reduce(operator.add, timeList))
bigY = int(functools.reduce(operator.add, distList))
delta = float(bigMaxX * bigMaxX - 4 * bigY)

x1 = (-bigMaxX + math.sqrt(delta)) / -2.
x2 = (-bigMaxX - math.sqrt(delta)) / -2.

if x1 == math.ceil(x1):
    x1 = x1 + 1.
if x2 == math.floor(x2):
    x2 = x2 - 1.

x1 = math.ceil(x1)
x2 = math.floor(x2)

print("day6 part 2:", x2 - x1 + 1)