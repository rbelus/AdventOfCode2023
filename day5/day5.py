import regex
import os
import sys

def intersects(xMin, xMax, yMin, yMax):
    return xMax >= yMin and yMax >= yMin

sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
input = open("input", "r")

curLine = input.readline()
numRegex = regex.compile(r"\d+")
mapRegex = regex.compile(r".*map:")

seedList = [int(seed) for seed in numRegex.findall(curLine)]

mappingRules = []
parsingMap = False
doneParsingNumbers = False
while curLine:
    if mapRegex.match(curLine) is None and not parsingMap:
        curLine = input.readline()
        continue
    elif not parsingMap:
        parsingMap = True
        curLine = input.readline()
        continue

    if curLine is not "\n":
        numList = numRegex.findall(curLine)
        # destStart = numList[0]
        # srcStart = numList[1]
        # rangeLength = numList[2]
        mappingRules.append([int(numList[0]), int(numList[1]), int(numList[2])])
    else:
        parsingMap = False
        doneParsingNumbers = True

    if doneParsingNumbers:
        for i in range(len(seedList)):
            for rule in mappingRules:
                if rule[1] <= seedList[i] < rule[1] + rule[2]:
                    seedList[i] = rule[0] + seedList[i] - rule[1]
                    break
        doneParsingNumbers = False
        mappingRules.clear()

    curLine = input.readline()

# BTW I added more blank lines at end of file, easier than fixing code :D

print("day5, part 1 : ", min(seedList))

input = open("input", "r")
curLine = input.readline()
numRegex = regex.compile(r"\d+")
mapRegex = regex.compile(r".*map:")

seedList = [int(seed) for seed in numRegex.findall(curLine)]

class _SeedRange:
    # stored in [a,b[ fashion
    a = 0
    b = 0
    transformed = False
    foundRule = False

    def __init__(self, a, b, t, f):
        self.a = a
        self.b = b
        self.transformed = t
        self.foundRule = f

    def GetSize(self):
        return self.b - self.a

class _MapRule:
    dstBegin = 0
    # stored in [a,b[ fashion
    srcA = 0
    srcB = 0

    def __init__(self, dst, a, b):
        self.dstBegin = dst
        self.srcA = a
        self.srcB = b

    def GetSrcSize(self):
        return self.srcB - self.srcA

rangeSeedList = []
for i in range(len(seedList) // 2):
    rangeStart = seedList[2*i]
    rangeLen = seedList[2*i+1]
    # rangeSeedList.append([rangeStart, rangeLen])
    rangeSeedList.append(_SeedRange(rangeStart, rangeStart + rangeLen, False, False))

totalSeeds = sum([seed.GetSize() for seed in rangeSeedList])

mappingList = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

mappingRules = []
parsingMap = False
doneParsingNumbers = False
curMapping = 0
while curLine:
    if mapRegex.match(curLine) is None and not parsingMap:
        curLine = input.readline()
        continue
    elif not parsingMap:
        parsingMap = True
        curLine = input.readline()
        continue

    if curLine is not "\n":
        numList = numRegex.findall(curLine)
        mappingRules.append(_MapRule(int(numList[0]), int(numList[1]), int(numList[1]) + int(numList[2])))
    else:
        parsingMap = False
        doneParsingNumbers = True

    # Instead of treating seeds individually like part1, compute new ranges
    if doneParsingNumbers:
        for rule in mappingRules:
            newRange = []
            for seed in rangeSeedList:
                a = seed.a
                b = seed.b
                if not seed.transformed:
                    if rule.srcA <= a and b <= rule.srcB:
                        """
                                    a-----------b
                                srcA---------------srcB
                        """
                        seed.foundRule = True
                        newA = rule.dstBegin + (a - rule.srcA)
                        newB = newA + (b - a)
                        newRange.append(_SeedRange(newA, newB, True, True))
                    elif a <= rule.srcA and rule.srcB <= b:
                        """
                                a-------------------b
                                    srcA-------srcB
                        """
                        seed.foundRule = True
                        if rule.srcA - a > 0:
                            newRange.append(_SeedRange(a, rule.srcA, False, True))
                        if rule.GetSrcSize() > 0: # is it even possible otherwise ?
                            newRange.append(_SeedRange(rule.dstBegin, rule.dstBegin + rule.GetSrcSize(), True, True))
                        if b - rule.srcB > 0:
                            newRange.append(_SeedRange(rule.srcB, b, False, True))
                    elif rule.srcA <= a <= rule.srcB <= b:
                        """
                                        a-------------b
                            srcA--------------srcB                        
                        """
                        seed.foundRule = True
                        if rule.srcB - a > 0:
                            newRange.append(_SeedRange(rule.dstBegin + (a - rule.srcA), rule.dstBegin + rule.GetSrcSize(), True, True))
                        if b - rule.srcB > 0:
                            newRange.append(_SeedRange(rule.srcB, b, False, True))
                    elif a <= rule.srcA <= b <= rule.srcB:
                        """
                                a-------------b
                                        srcA----------srcB                        
                        """
                        seed.foundRule = True
                        if rule.srcA - a > 0:
                            newRange.append(_SeedRange(a, rule.srcA, False, True))
                        if b - rule.srcA > 0:
                            newRange.append(_SeedRange(rule.dstBegin, rule.dstBegin + (b - rule.srcA), True, True))
            # Update seed list
            for seed in rangeSeedList:
                if not seed.foundRule:
                    newRange.append(_SeedRange(seed.a, seed.b, seed.transformed, False))
            rangeSeedList.clear()
            rangeSeedList = newRange
            for seed in rangeSeedList:
                seed.foundRule = False

            # sizes = [seed.GetSize() for seed in rangeSeedList]
            # curTotalSeeds = sum([seed.GetSize() for seed in rangeSeedList])
            # assert curTotalSeeds == totalSeeds

        for seed in rangeSeedList:
            seed.foundRule = False
            seed.transformed = False

        doneParsingNumbers = False
        mappingRules.clear()

    curLine = input.readline()

rangeSeedList.sort(key=lambda s: s.a)
print("day5, part 2 : ", rangeSeedList[0].a)
