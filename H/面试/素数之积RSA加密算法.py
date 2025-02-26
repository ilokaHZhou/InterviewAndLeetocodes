import math

# 函数：检查一个数是否为素数
def is_prime(num):
    if num <= 3:
        return num > 1
    if num % 6 != 1 and num % 6 != 5:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

num = int(input())

# 如果数字本身就是素数，那么它不能被分解
if is_prime(num):
    print("-1 -1")
else:
    # 分解数字
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            j = num // i
            # 检查 i 和 j 是否都是素数
            if is_prime(i) and is_prime(j):
                print(f"{min(i, j)} {max(i, j)}")
                break
    else:
        print("-1 -1")