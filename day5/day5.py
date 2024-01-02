import regex
import os
import sys

def intersects(xMin, xMax, yMin, yMax):
    return xMax >= yMin and yMax >= yMin

sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
input = open("inputTest", "r")

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

input = open("inputTest", "r")
curLine = input.readline()
numRegex = regex.compile(r"\d+")
mapRegex = regex.compile(r".*map:")

seedList = [int(seed) for seed in numRegex.findall(curLine)]

rangeSeedList = []
for i in range(len(seedList) // 2):
    rangeStart = seedList[2*i]
    rangeLen = seedList[2*i+1]
    rangeSeedList.append([rangeStart, rangeLen])

totalSeeds = sum([seed[1] for seed in rangeSeedList])

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

    # Instead of treating seeds individually like part1, compute new ranges
    if doneParsingNumbers:
        # newRanges = []
        print(rangeSeedList)
        # print(mappingRules)

        if sum([seed[1] for seed in rangeSeedList]) != totalSeeds:
            print("problem")

        transformedRangeSeedList = rangeSeedList.copy()
        for i in range(len(rangeSeedList)):
            for rule in mappingRules:
                minRule, maxRule = rule[1], rule[1] + rule[2] - 1
                minSeed, maxSeed = rangeSeedList[i][0], rangeSeedList[i][0] + rangeSeedList[i][1] - 1
                # Test ranges intersect and create new ranges
                # Given below tests, intersect test not necessary..
                if intersects(minRule, maxRule, minSeed, maxSeed):
                    # Create new ranges
                    if minRule <= minSeed and maxSeed <= maxRule:
                        # 1 range to create
                        transformedRangeSeedList[i] = [rule[0] + minSeed - minRule, maxSeed - minSeed + 1]
                    elif minSeed <= minRule and maxRule <= maxSeed:
                        # 3 ranges to create
                        transformedRangeSeedList[i] = [minSeed, minRule - minSeed]
                        transformedRangeSeedList.append([rule[0], rule[2] + 1]) # Rule applied entirely to this range
                        transformedRangeSeedList.append([maxRule + 1, maxSeed - maxRule])
                    elif minSeed <= maxRule <= maxSeed:
                        # 2 ranges to create
                        transformedRangeSeedList[i] = [rule[0] + maxRule - minSeed, maxRule - minSeed + 1] # Rule applied partially to this range
                        transformedRangeSeedList.append([maxRule + 1, maxSeed - maxRule])
                        # newRanges.append([minSeed, maxRule - minSeed, rule[0] + maxRule - minSeed, maxRule - minSeed]) # Rule applied partially to this range
                        # newRanges.append([maxRule, maxSeed - maxRule])
                    elif minSeed <= minRule <= maxSeed:
                        # 2 ranges to create
                        transformedRangeSeedList[i] = [minSeed, minRule - minSeed]
                        transformedRangeSeedList.append([rule[0], maxSeed - minRule + 1]) # Rule applied partially to this range
                        # newRanges.append([minSeed, minRule - minSeed])
                        # newRanges.append([minRule, maxSeed - minRule, rule[0], maxSeed - minRule]) # Rule applied partially to this range
                    #elif minRule <= minSeed and maxSeed <= maxRule:
                        # 1 range to create
                    #    transformedRangeSeedList[i] = [rule[0] + minSeed - minRule, maxSeed - minSeed]
                        # newRanges.append([minSeed, maxSeed - minSeed, rule[0] + minSeed - minRule, maxSeed - minSeed])

        rangeSeedList.clear()
        rangeSeedList = transformedRangeSeedList

        # # Transform range seed list to take into account rules
        # newRanges.sort()
        # rangeSeedList.sort()
        # transformedRangeSeedList = rangeSeedList.copy()
        #
        # for i in range(len(rangeSeedList)):
        #     for transformedRanges in newRanges:
        #         if intersects(rangeSeedList[i][0], rangeSeedList[i][0] + rangeSeedList[i][1], transformedRanges[0], transformedRanges[1]):
        #             minTsf, maxTsf = transformedRanges[0], transformedRanges[1]
        #             minSeed, maxSeed = rangeSeedList[i][0], rangeSeedList[i][1]
        #             if minSeed <= minTsf and maxTsf <= maxSeed:
        #                 # 3 ranges to transform
        #                 transformedRangeSeedList[i][1] = minTsf -
        #                 transformedRangeSeedList.append([transformedRanges[]])
        #             elif minSeed <= maxTsf <= maxSeed:
        #                 # 2 ranges to create
        #
        #             elif minSeed <= minTsf <= maxSeed:
        #                 # 2 ranges to create
        #
        #             elif minTsf <= minSeed and maxSeed <= maxTsf:
        #                 # 1 range to create


        doneParsingNumbers = False
        mappingRules.clear()

    curLine = input.readline()

print("day5, part 2 : ", rangeSeedList)
