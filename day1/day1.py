import regex
import os
import sys

sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
input = open("input", "r")

digitRegex = regex.compile(r"(one|two|three|four|five|six|seven|eight|nine|\d)")
lexicalDict = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
}

def ConvertMatchToInt(m):
    if len(m) == 1:
        return int(m)
    else:
        return lexicalDict[m]
    
totalCalibrationValue = 0
for line in input.readlines():
    calibrationValue = 0
    m = regex.search(digitRegex, line)
    calibrationValue += 10 * ConvertMatchToInt(m.group(0))
    m = regex.findall(digitRegex, line, overlapped=True)
    calibrationValue += ConvertMatchToInt(m[::-1][0])
    print(calibrationValue)
    totalCalibrationValue += calibrationValue
    

print(totalCalibrationValue)