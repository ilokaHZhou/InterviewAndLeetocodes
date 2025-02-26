counts = list(map(int, input().split()))

totalPass = sum(counts)

numberOfPeople = len(counts)
peopleCounts = [0] * numberOfPeople

currentNumber = 1
currentIndex = 0
while totalPass > 0:
    if currentNumber % 7 == 0 or str(currentNumber).find('7') != -1:
        totalPass -= 1
        peopleCounts[currentIndex] += 1
    currentNumber += 1
    currentIndex = (currentIndex + 1) % numberOfPeople

output = ' '.join(map(str, peopleCounts))
print(output)