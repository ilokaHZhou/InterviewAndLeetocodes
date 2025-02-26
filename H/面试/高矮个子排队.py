import re

s = input()
if not re.match(r"[0-9\s]+", s):
    print("[]")
    exit()

heights = list(map(int, s.split()))

i = 0
j = 1

while j < len(heights):
    if heights[i] != heights[j] and (heights[i] > heights[j]) != (i % 2 == 0):
        heights[i], heights[j] = heights[j], heights[i]
        
    i += 1
    j += 1

result = " ".join(map(str, heights))
print(result)