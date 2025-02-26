import sys

for line in sys.stdin:
    # 读取输入的n和m，n代表牌的数量，m代表小明手中牌上的数字
    n, m = map(int, line.split())

    # 读取后续发的n张牌的数字
    cardNumbers = list(map(int, input().split()))

    # 使用列表来记录余数的出现情况
    remainderExists = [False] * m

    sum = 0
    found = False
    for cardNumber in cardNumbers:
        sum += cardNumber  # 将当前牌的数字累加到sum中
        remainder = sum % m  # 计算当前和的余数
        if remainderExists[remainder]:  # 如果之前已经存在相同的余数，说明存在连续的若干张牌和可以整除m
            found = True
            break
        else:
            remainderExists[remainder] = True  # 将当前余数标记为已存在

    print(1 if found else 0)