def buy_chickens():
    for x in range(0, 21):  # 公鸡最多买 20 只
        for y in range(0, 34):  # 母鸡最多买 33 只
            z = 100 - x - y  # 小鸡的数量
            if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:  # 满足条件
                print(x, y, z)  # 输出解


# 调用函数
buy_chickens()
