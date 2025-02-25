def arithmetic_sequence_sum(n):
    first_term = 2  # 首项
    last_term = 3 * n - 1  # 末项
    # 等差数列求和公式：S = n * (a1 + an) / 2
    return n * (first_term + last_term) // 2


# 输入处理
n = int(input())
print(arithmetic_sequence_sum(n))
