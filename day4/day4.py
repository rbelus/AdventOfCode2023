import regex
import os
import sys

sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
input = open("input", "r")

numRegex = regex.compile(r'\d+')

totalCardValues = 0

# Blah blah we know input is formatted
nbWinningNumbers = 10

cardCounter = [1 for i in range(sum(1 for _ in open('input')))]

cardNum = 0
for line in input.readlines():
    allCardNumbers = numRegex.findall(line)

    winningCardNumbers = allCardNumbers[1:nbWinningNumbers+1]
    scratchedCardNumbers = allCardNumbers[nbWinningNumbers+1::]

    nbMatches = len(set(winningCardNumbers) & set(scratchedCardNumbers)) -1

    # Floor to prevent square root when 0 matches
    cardValue = int(pow(2, nbMatches))
    totalCardValues += cardValue

    for i in range(1, nbMatches + 2):
        if cardNum + i < len(cardCounter):
            cardCounter[cardNum + i] += cardCounter[cardNum]

    cardNum += 1

print("Day 4, part 1: ", str(totalCardValues))
print("Day 4, part 2: ", str(sum(cardCounter)))