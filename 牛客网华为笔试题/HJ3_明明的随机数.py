import random

def quicksort_recursive(arr):
    if len(arr) <= 1:
        return arr
    # randint 会包含两个边界所以是(0, len(arr) - 1)
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    mid = [y for y in arr if y == pivot]
    right = [z for z in arr if z > pivot]
    return quicksort_recursive(left) + mid + quicksort_recursive(right)


while True:
    try:
        n = int(input().strip())
        numbers = []
        for i in range(n):
            number = int(input().strip())
            numbers.append(number)
        unique_numbers_set = set(numbers)
        unique_numbers_list = list(unique_numbers_set)
        sorted_list = quicksort_recursive(unique_numbers_list)
        for num in sorted_list:
            print(num)

    except:
        break
