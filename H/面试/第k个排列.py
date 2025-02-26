n = int(input())
k = int(input())


if n == 1:
    print("1")
    exit()

nums = [i+1 for i in range(n)]
result = []

def generatePermutations(nums, current, result, k):
    if len(nums) == 0:
        result.append(current)
        return

    for i in range(len(nums)):
        num = nums[i]
        newNums = nums[:i] + nums[i+1:]
        generatePermutations(newNums, current + str(num), result, k)

        if len(result) == k:
            return

generatePermutations(nums, "", result, k)

result.sort()
print(result[k-1])