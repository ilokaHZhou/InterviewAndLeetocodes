import random

"""
快速排序的平均时间复杂度（O(n*log2(n)))和空间复杂度（O(log2(n)))
最坏情况下的时间复杂度（O(n^2)）和空间复杂度（O(n)）
"""

# 递归解法 （空间复杂度高，需要大量额外空间储存left mid和right数组）
def quicksort_recursive(arr):
    if len(arr) <= 1:
        return arr
    # 随机选择 pivot, randint 会包含两个边界所以是(0, len(arr) - 1)
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_recursive(left) + middle + quicksort_recursive(right)

# -----------------------

# 递归解法2（不需要额外空间，数组本身元素交换）
def quicksort_recursive2(nums, left, right):
    if left < right:
        # 选择随机数字作为比较轴进行排序，排完返回对应数字的index
        l_index,  r_index = partition2(nums, left, right)
        quicksort_recursive2(nums, left, l_index - 1)
        quicksort_recursive2(nums, r_index + 1, right)

def partition2(arr, left, right):
    pivot_index = random.randint(left, right)
    pivot = arr[pivot_index]

    # 这两个是待排序子序列的左右索引，使用这个可以进行三路排序，用来避免数组里全是相同数字
    # 全相同数字的话l_index，r_index排完依旧等于left，right，外层递归判断 if left < right 会在下一次递归调用时直接跳出
    l_index = left
    r_index = right

    # 前i个数用来存比pivot小的数
    i = left
    while i <= r_index:
        if arr[i] < pivot:
            arr[i], arr[l_index] = arr[l_index], arr[i]
            l_index += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[r_index] = arr[r_index], arr[i]
            r_index -= 1
        else:
            i += 1
    # 返回的不只是pivot的index，而是l_index, r_index
    return l_index, r_index

# -----------------------

# 循环解法
def quicksort_iterative(arr):
    stack = [(0, len(arr) - 1)]
    
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        
        # 随机选择 pivot 并分区
        pivot_index = partition(arr, start, end)
        stack.append((start, pivot_index - 1))
        stack.append((pivot_index + 1, end))
    
    return arr

def partition(arr, start, end):
    # 随机选择 pivot
    pivot_index = random.randint(start, end)
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]  # 将 pivot 放到最后
    pivot = arr[end]
    i = start - 1
    
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


# 示例用法
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort_recursive(arr)
print(sorted_arr)

# 示例用法
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort_iterative(arr)
print(sorted_arr)


# 测试 2：所有元素相等
arr = [5, 5, 5, 5, 5, 5, 5]
quicksort_recursive2(arr, 0, len(arr) - 1)
print("Sorted array (所有元素相等):", arr)

# 测试 3：大量重复元素
arr = [4, 2, 2, 8, 3, 3, 1, 4, 4]
quicksort_recursive2(arr, 0, len(arr) - 1)
print("Sorted array (大量重复元素):", arr)