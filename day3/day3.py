import regex
import os
import sys

sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
input = open("input", "r")

numberRegex = regex.compile(r"\d+")
symbolRegex = regex.compile(r"[^\d\.\n]")

symbolPositions = []
numberSpans = []

# UNOPTIMIZED, should only parse lines 3 by 3 ._.

# parse file to store all numbers and symbols
y = 0
for line in input.readlines():
    lineNumbers = regex.findall(numberRegex, line)
    lineSymbols = regex.findall(symbolRegex, line)

    for symbol in lineSymbols:
        x = line.find(symbol)
        symbolPositions.append([x,y,symbol])
        line = line.replace(symbol, '.', 1)

    for number in lineNumbers:
        x_start = line.find(number)
        x_end = x_start + len(number) - 1
        numberSpans.append([x_start, x_end, y, number])
        replaceString = "".zfill(len(number))
        line = line.replace(number, replaceString, 1)

    y += 1

totalPartNumberSum = 0
possibleGearNumbers = []
# parse found numbers to check if symbols are next
for partNumber in numberSpans:
    for symbol in symbolPositions:
        xSymbol, ySymbol = symbol[0], symbol[1]
        xNumMin, xNumMax, yNumber = partNumber[0], partNumber[1], partNumber[2]
        # We reached too far : no symbols will be next
        if ySymbol > yNumber + 1:
            break
        # We did not reach this line yet
        if ySymbol < yNumber - 1:
            continue
        # Is symbol in range ?
        if xNumMin - 2 < xSymbol < xNumMax + 2:
            totalPartNumberSum += int(partNumber[3])
            if symbol[2] == '*':
                possibleGearNumbers.append(partNumber)
            break

print("Part 1 of day3 : ", totalPartNumberSum)

# somewhat same as above but with gears, could create this list while parsing above but heh i like making comprehensions
gearList = [symbol for symbol in symbolPositions if symbol[2] == '*']

# Let's just parse already validated Numbers shall we ? :)
totalGearPower = 0
for gear in gearList:
    matchedNumbers = []
    for gearNumber in possibleGearNumbers:
        xGear, yGear = gear[0], gear[1]
        xNumMin, xNumMax, yNumber = gearNumber[0], gearNumber[1], gearNumber[2]
        # We reached too far : no symbols will be next
        if yNumber > yGear + 1:
            break
        # We did not reach this line yet
        if yNumber < yGear - 1:
            continue
        # Is symbol in range ?
        if xNumMin - 2 < xGear < xNumMax + 2:
            matchedNumbers.append(gearNumber)

    if len(matchedNumbers) == 2:
        totalGearPower += int(matchedNumbers[0][3]) * int(matchedNumbers[1][3])

print("Part 2 of day3 : ", totalGearPower)
