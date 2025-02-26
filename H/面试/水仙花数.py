def isNarcissusNumber(num, n):
    sum = 0
    numStr = str(num)

    for i in range(n):
        sum += int(numStr[i]) ** n

    return sum == num
n = int(input())
m = int(input())

if n < 3 or n > 7:
    print("-1")
    exit()

start = 10 ** (n - 1)
end = 10 ** n

narcissusList = []

for i in range(start, end):
    if isNarcissusNumber(i, n):
        narcissusList.append(i)

size = len(narcissusList)

if size == 0:
    print("-1")
    exit()

print(narcissusList[size - 1] if m >= size else narcissusList[m])