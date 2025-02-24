def gcd(a, b):  # 计算最大公约数
    while b:  # 辗转相除法
        a, b = b, a % b
    return a


def lcm(a, b):  # 计算最小公倍数
    return a * b // gcd(a, b)  # 最小公倍数 = 两数乘积 / 最大公约数


# 输入处理
a, b = map(int, input().split())
print(lcm(a, b))
