def is_automorphic_number(n):
    square = n * n  # 计算平方
    # 判断平方的末尾是否等于原数
    return str(square).endswith(str(n))


def count_automorphic_numbers(n):
    count = 0  # 自守数计数器
    for i in range(n + 1):  # 遍历 0 到 n
        if is_automorphic_number(i):  # 如果是自守数
            count += 1  # 计数器加 1
    return count  # 返回自守数的个数


# 输入处理
n = int(input())
print(count_automorphic_numbers(n))
