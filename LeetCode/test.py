import random

def quicksort(arr, low, high):
    # 递归终止条件：子数组长度为 0 或 1
    if low >= high:
        return

    # 随机选择基准元素，并将其交换到末尾
    pivot_index = random.randint(low, high)  # 随机选择一个索引
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # 将基准元素放到最后

    # 划分序列，返回基准元素的最终位置
    pivot_index = partition(arr, low, high)

    # 递归排序小于基准的部分
    quicksort(arr, low, pivot_index - 1)

    # 递归排序大于基准的部分
    quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    # 选择基准元素（此时基准元素已经在最后的位置）
    pivot = arr[high]
    i = low  # i 指向小于基准部分的末尾

    # 遍历序列，将小于基准的元素放到左边
    for j in range(low, high):
        if arr[j] == pivot:
            i += 1
        elif arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素
            i += 1

    # 将基准元素放到正确的位置
    arr[i], arr[high] = arr[high], arr[i]

    # 返回基准元素的最终位置
    return i


# 测试快速排序
arr = [5,1,1,2,0,0]
quicksort(arr, 0, len(arr) - 1)
print("排序后的数组:", arr)