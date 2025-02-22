import sys

def soda_bottles(n):
    total = 0
    while n >= 3:
        # 计算当前可以兑换的汽水瓶数
        exchange = n // 3
        total += exchange
        # 更新剩余的空瓶数
        n = n % 3 + exchange
    # 如果剩余 2 个空瓶，可以借一个瓶子兑换
    if n == 2:
        total += 1
    return total


for line in sys.stdin:
    n = int(line.strip())
    if n == 0: # n = 0代表输入结束
        break
    print(soda_bottles(n))
