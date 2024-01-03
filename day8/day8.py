import regex
import os
import sys
import math
import functools
import operator
from collections import deque
import numpy

class Node:
    nodeDict = {}

    def __init__(self, name, leftName, rightName):
        self.name = name
        self.leftName = leftName
        self.rightName = rightName

        self.nodeDict[self.name] = self

    def Left(self):
        return self.nodeDict[self.leftName]

    def Right(self):
        return self.nodeDict[self.rightName]

    def Display(self):
        return self.name + " : (" + self.leftName + ', ' + self.rightName + ')'

sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
input = open("input", "r")

moveSet = deque(input.readline().strip())

nodeRegex = regex.compile(r"(?<node>\w\w\w).*(?<left>\w\w\w).*(?<right>\w\w\w)")

nodeList = []
for line in input.readlines():
    match = nodeRegex.match(line)
    if match is not None:
        nodeList.append(Node(match.group('node'), match.group('left'), match.group('right')))

#Follow directions !
nbMove = 0
if False:
    curNode = Node.nodeDict['AAA']
    while curNode.name != 'ZZZ':
        if moveSet[0] == 'L':
            curNode = curNode.Left()
        if moveSet[0] == 'R':
            curNode = curNode.Right()
        moveSet.rotate(-1)
        nbMove += 1

print("Day 8 part 1:", nbMove)

# Reset for part 2
input = open("input", "r")
moveSet = deque(input.readline().strip())

startNodes = [Node.nodeDict[key] for key in Node.nodeDict.keys() if key.endswith('A')]

# Figure out shortest path to node ending in z before it loops
moveToZ = [0 for node in startNodes]
for i in range(len(startNodes)):
    nbMove = 0
    nodeMoveSet = moveSet.copy()
    while True:
        if nodeMoveSet[0] == 'L':
            startNodes[i] = startNodes[i].Left()
        if nodeMoveSet[0] == 'R':
            startNodes[i] = startNodes[i].Right()
        nodeMoveSet.rotate(-1)
        nbMove += 1
        if startNodes[i].name.endswith('Z'):
            moveToZ[i] = nbMove
            break

lcm = numpy.lcm.reduce(moveToZ)
# startNodes = [Node.nodeDict[key] for key in Node.nodeDict.keys() if key.endswith('A')]

print("Day 8 part 2:", numpy.lcm.reduce(moveToZ))