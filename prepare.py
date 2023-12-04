import requests
import argparse
import sys
import os

def PrepareDay(day, path):
    # Create folder
    folder = os.path.abspath(path)
    if os.path.exists(folder):
        newDayFolder = os.path.join(folder, "day%d"%day)
        if not os.path.exists(newDayFolder):
            os.mkdir(newDayFolder)
        file = open(os.path.join(newDayFolder, "input"), 'w')
        # Fetch input
        for tryCounts in range(0, 1):
            print("Attempt %s reading input" % tryCounts)
            try:
                testURL = "https://adventofcode.com/2023/day/%d/input"%day
                httpRequest = requests.get(testURL, cookies={'session':"53616c7465645f5f06cb4811e4ffa155977129cd261367b38a3df19126efb2cf9a0f1fcd9197b10600853b9c9e91605d0bf583d0485c71176c6e1844b7ce065b"})
                file.writelines(httpRequest.text)
                break
            except Exception as e:
                print("Encountered : %s" % str(e))

parser = argparse.ArgumentParser(description='Prepare folders with input.')
parser.add_argument('day', metavar='N', type=int, help='day to prepare')
parser.add_argument('path', type=str)
args = parser.parse_args()
PrepareDay(args.day, args.path)