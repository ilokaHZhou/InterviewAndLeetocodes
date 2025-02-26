import sys

line = input()
numStrArray = line.split(",")
map = {}
maxScore = 0
for m in range(len(numStrArray)):
    num = int(numStrArray[m])
    if m < 3:
        if m == 0:
            maxScore = max(0, num)
        else:
            maxScore = max(0, (maxScore + num))
    else:
        maxScore = max((maxScore + num), map[m - 2])
    map[m + 1] = maxScore
sys.stdout.write(str(maxScore))