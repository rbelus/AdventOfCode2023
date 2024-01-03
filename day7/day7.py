import regex
import os
import sys
import math
import functools
import operator

class Hand:
    _typeDict = {
        "High": 0,
        "Pair": 1,
        "2Pair": 2,
        "3Kind": 3,
        "Full": 4,
        "4Kind": 5,
        "5Kind": 6
    }

    class _Card:
        # for part 1
        # _valueDict = {"2" : 0, "3" : 1, "4" : 2, "5" : 3, "6" : 4, "7" : 5, "8" : 6, "9" : 7, "T" : 8, "J" : 9, "Q" : 10, "K" : 11, "A" : 12}
        # for part 2
        _valueDict = {"2" : 0, "3" : 1, "4" : 2, "5" : 3, "6" : 4, "7" : 5, "8" : 6, "9" : 7, "T" : 8, "J" : -1, "Q" : 10, "K" : 11, "A" : 12}

        def __init__(self, value):
            self.value = value

        def InternalValue(self):
            return self._valueDict[self.value]

    def ComputeType(self):
        counter = {}
        for card in self.cards:
            curCount = counter.get(card.value, 0)
            counter[card.value] = curCount + 1
        nbJoker = counter.get("J", 0)
        if nbJoker > 0:
            counter.pop("J")
        values = list(counter.values())
        if nbJoker == 5 or max(values) + nbJoker == 5:
            return "5Kind"
        if max(values) + nbJoker == 4:
            return "4Kind"
        if max(values) + nbJoker == 3 and min(values) == 2:
            return "Full"
        if max(values) + nbJoker == 3:
            return "3Kind"
        if max(values) == 2 and len(values) <= 3:#and len(counter.values()) <= 3:
            return "2Pair"
        if max(values) + nbJoker == 2:
            return "Pair"
        return "High"
    def Display(self):
        strDisplay = ""
        for c in self.cards:
            strDisplay += c.value
        return strDisplay

    def __init__(self, hand, bid):
        self.cards = []
        for char in hand:
            self.cards.append(self._Card(char))
        self.bid = bid
        self.type = self.ComputeType()

    def cmp(self, other):
        if self._typeDict[self.type] < self._typeDict[other.type]:
            return -1
        if self._typeDict[self.type] > self._typeDict[other.type]:
            return  1

        # compute card by card
        for i in range(len(self.cards)):
            if self.cards[i].InternalValue() < other.cards[i].InternalValue():
                return -1
            if self.cards[i].InternalValue() > other.cards[i].InternalValue():
                return 1
        return 0


sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
input = open("input", "r")

handList = []
for line in input.readlines():
    h, b = line.split(" ")
    handList.append(Hand(h, int(b)))

print([hand.Display() + " " + hand.type for hand in handList])
handList.sort(key=functools.cmp_to_key(Hand.cmp))
print([hand.Display() + " " + hand.type for hand in handList])

# Compute winnings
totalWinning = 0
for i in range(1, len(handList) + 1):
    totalWinning += i * handList[i-1].bid

# Need to remove joker
# print("day7 part1 : ", totalWinning)

print("day7 part2 : ", totalWinning)
