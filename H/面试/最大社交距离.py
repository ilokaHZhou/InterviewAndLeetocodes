import math

# 读取输入
seatNum = int(input())  # 座位总数
str = input()  # 座位占用和离开的操作序列
seatOrLeave = list(map(int, str[1:-1].split(",")))  # 将字符串转换为整数数组

# 初始化
seat = []  # 存储已占用的座位
ans = -1  # 下一个人的最佳座位号

for sol in seatOrLeave:  # 遍历座位占用和离开的操作序列
    if sol != 1:
        # 如果sol为负数，表示有员工离开，移除对应座位号
        seat.remove(-sol)
    else:
        # 如果sol为1，表示有员工进入，需要找到最佳座位
        if not seat:
            # 如果会议室为空，新员工坐在0号座位
            ans = 0
        else:
            # 如果会议室不为空，找到最大的空闲区间
            max_distance = seat[0]  # 初始化最大距离为第一个座位号
            ans = 0  # 初始化最佳座位号为0
            for i in range(len(seat)):
                if i == len(seat) - 1:
                    # 检查最后一个座位到座位总数之间的距离
                    distance = seatNum - 1 - seat[i]
                else:
                    # 检查相邻座位之间的距离
                    distance = (seat[i + 1] - seat[i]) // 2
                if distance > max_distance:
                    # 更新最大距离和最佳座位号
                    max_distance = distance
                    if i == len(seat) - 1:
                        ans = seatNum - 1
                    else:
                        ans = seat[i] + distance

        # 如果会议室已满，输出-1
        if len(seat) == seatNum:
            ans = -1
        else:
            # 将新员工的座位号加入到座位列表，并排序
            seat.append(ans)
            seat.sort()

print(ans)
