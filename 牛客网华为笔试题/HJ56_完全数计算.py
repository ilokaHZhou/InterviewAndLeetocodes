def is_perfect_number(num):
    if num < 2:
        return False
    divisors = {1}  # 初始化约数集合
    for i in range(2, int(num ** 0.5) + 1):  # 遍历可能的约数
        if num % i == 0:
            divisors.add(i)  # 添加约数
            divisors.add(num // i)  # 添加配对的约数
    return sum(divisors) == num  # 判断是否为完全数


def count_perfect_numbers(n):
    count = 0  # 完全数计数器
    for num in range(2, n + 1):  # 遍历 2 到 n，1没有除了自身以外的约数
        if is_perfect_number(num):
            count += 1  # 统计完全数
    return count


# 输入处理
n = int(input())
print(count_perfect_numbers(n))
