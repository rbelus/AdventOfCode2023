import regex
import os
import sys

sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
input = open("input", "r")

idRegex = regex.compile(r"Game (\d+):")
gameRegex = regex.compile(r"((\d+) (blue|red|green))(, )?|;")

colorDict = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

totalPossibleGames = 0
for line in input.readlines():
    m = regex.search(idRegex, line)
    gameID = m.group(1)

    parsed = regex.findall(gameRegex, line)
    newSet = True
    impossible = False
    for gameStep in parsed:
        if len(gameStep[0]) > 2: # correct game step ish
            newSet = False
            if int(gameStep[1]) > colorDict[gameStep[2]]:
                impossible = True
        else:
            newSet = True

    if not impossible:
        totalPossibleGames += int(gameID)

print("Part 1 : " + str(totalPossibleGames))

input = open("input", "r")

totalPower = 0
for line in input.readlines():
    colorDict = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }
    m = regex.search(idRegex, line)
    gameID = m.group(1)

    parsed = regex.findall(gameRegex, line)
    for gameStep in parsed:
        if len(gameStep[0]) > 2: # correct game step ish
            colorDict[gameStep[2]] = max(int(gameStep[1]), colorDict[gameStep[2]])
    totalPower += colorDict['red'] * colorDict['green'] * colorDict['blue']

print("Part 2 : " + str(totalPower))