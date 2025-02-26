chars = input()  # 输入字符串，包含大雁的叫声
quack = "quack"  # 大雁叫声的顺序
states = [0] * len(quack)  # 用于跟踪每个字符当前出现的状态，初始为全0
dp = []  # 动态规划数组，记录每次完成一个“quack”所需要的最少大雁数量
max_ = 0  # 记录当前最大的大雁数量

for i in range(len(chars)):
    index = quack.find(chars[i])  # 找到当前字符在“quack”中的位置
    if index == -1:  # 如果字符不在“quack”中，直接返回-1
        print(-1)
        exit()

    if index == 0:  # 如果是“q”，表示一个新的大雁叫声的开始
        states[index] += 1  # 对应位置状态加1
    else:
        if states[index - 1]:  # 如果前一个字符的位置状态存在（即有前置字符）
            states[index - 1] -= 1  # 前一个字符的状态减1
            states[index] += 1  # 当前字符的状态加1

        if quack[-1] == chars[i]:  # 如果当前字符是“k”，即完成了一个“quack”
            if states[-1] != 0:  # 确保有完整的大雁叫声
                temp = [t for t in states]  # 复制当前状态
                temp[-1] = 0  # 将最后一个字符的状态设为0，表示一个大雁叫声结束
                max_ = max(max_, sum(temp))  # 更新最大的大雁数量
                for j in range(i, len(chars)):  # 从当前位置向后继续检查是否有完整的“quack”
                    index = quack.find(chars[j])
                    if temp[index - 1]:  # 如果前一个字符的位置状态存在
                        temp[index - 1] -= 1  # 前一个字符的状态减1
                        temp[index] += 1  # 当前字符的状态加1
                    if temp[-1] == max_:  # 如果状态达到最大值
                        break  # 结束当前循环
                dp.append(temp[-1] + 1)  # 将当前计算的结果记录到动态规划数组
                states[-1] -= 1  # 减少完成的“quack”计数

# 输出最大的大雁数量，如果没有找到有效的“quack”，则返回-1
print(max(dp) if dp else -1)