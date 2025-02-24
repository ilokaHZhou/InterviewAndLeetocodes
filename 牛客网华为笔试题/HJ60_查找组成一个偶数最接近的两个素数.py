def is_prime(num):  # 判断是否为素数
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_closest_primes(even_num):
    for i in range(even_num // 2, 1, -1):  # 从中间向小遍历
        if is_prime(i) and is_prime(even_num - i):  # 找到两个素数
            return i, even_num - i  # 返回最接近的两个素数
    return 0, 0


# 输入处理
even_num = int(input())
result = find_closest_primes(even_num)
print(result[0])
print(result[1])
