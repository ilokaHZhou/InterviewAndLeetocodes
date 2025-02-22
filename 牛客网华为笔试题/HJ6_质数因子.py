import math

# 读取输入
n = int(input())

# 输出所有质数因子
def prime_factors(n):
    factors = []
    # 处理 2 的因子
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # 处理奇数因子
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    # 如果 n 是质数且大于 2
    if n > 2:
        factors.append(n)
    return factors

# 获取质数因子并输出
factors = prime_factors(n)
for factor in sorted(factors):
    print(factor, end=' ')