import random

"""
快速排序的平均时间复杂度（O(n*log2(n)))和空间复杂度（O(log2(n)))
最坏情况下（完全逆序排序，选的基准在序列另一头）的时间复杂度（O(n^2)）和空间复杂度（O(n)）

最坏情况发生在每次划分都极度不平衡时，例如每次选择的基准元素都是当前序列的最大或最小值。这种情况下，递归树的深度为n，每层仍需O(n)的时间，总复杂度为O(n²)。

    逆序和顺序的情况
    逆序序列：如果序列已经是逆序的，且每次选择第一个元素作为基准，那么每次划分都会将序列分成一个空子序列和一个包含剩余元素的子序列，导致复杂度退化为O(n²)。

    顺序序列：如果序列已经是顺序的，且每次选择最后一个元素作为基准，同样会导致每次划分极度不平衡，复杂度退化为O(n²)。


如何避免最坏情况？
    1. 随机选择基准：通过随机选择基准元素，可以减少最坏情况发生的概率。

    2. 三数取中法：选择序列的头、尾、中三个元素的中位数作为基准，也能有效避免最坏情况。 

专门用于处理包含大量重复元素的序列？
    三路排序法，只需要一次遍历，时间复杂度为 O(n)。
"""

# 递归解法1 （空间复杂度高，需要大量额外空间储存left mid和right数组）
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

# 递归解法2 （不需要额外空间，数组本身元素交换）

def quicksort(arr, low, high):
    if low >= high:
        return

    # 随机选择基准元素，并将其交换到末尾
    pivot_index = random.randint(low, high)  # 随机选择一个索引
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # 将基准元素放到最后

    pivot_index = partition(arr, low, high)
    quicksort(arr, low, pivot_index - 1)
    quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    # 选择基准元素（此时基准元素已经在最后的位置）
    pivot = arr[high]
    i = low  # i 指向小于基准部分的末尾

    # 遍历序列，将小于基准的元素放到左边
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素
            i += 1

    # 将基准元素放到正确的位置
    arr[i], arr[high] = arr[high], arr[i]
    return i

# -----------------------

# 递归解法3（不需要额外空间，数组本身元素交换, 三路排序处理有大量重复元素的序列）
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

# 循环解法（不需要额外空间，数组本身元素交换）
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