def merge_arrays(arr1, arr2):
    merged = sorted(set(arr1 + arr2))  # 合并数组并去重、排序
    return "".join(map(str, merged))  # 转换为字符串输出


# 输入处理
n1 = int(input())
arr1 = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))

# 输出结果
print(merge_arrays(arr1, arr2))