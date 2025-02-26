import re

str = input()
k = int(input())
charSet = set(str)
charMap = {}
for c in charSet:
    reg = re.compile(c + "+")
    it = re.finditer(reg, str)
    for match in it:
        repeatTimes = len(match.group())
        if c in charMap:
            charMap[c] = max(charMap[c], repeatTimes)
        else:
            charMap[c] = repeatTimes
values = list(charMap.values())
values.sort(reverse=True)
rt = -1 if k > len(values) else values[k-1]
print(rt)