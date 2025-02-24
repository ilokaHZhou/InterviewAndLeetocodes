def find_first_even(n):
    if n <= 2:
        return -1
    # 规律：从第3行开始，偶数出现的位置为 2, 3, 2, 4 的循环
    pattern = [2, 3, 2, 4]
    return pattern[(n - 3) % 4]


# 输入处理
n = int(input())
print(find_first_even(n))
