def ball_distance_and_height(initial_height):
    total_distance = 0  # 总路程
    current_height = initial_height  # 当前高度
    for _ in range(5):  # 模拟 5 次落地
        total_distance += current_height  # 下落距离，下
        current_height /= 2  # 反弹高度减半
        total_distance += current_height  # 反弹距离, 上
    total_distance -= current_height  # 第 5 次反弹后不计入总路程
    return total_distance, current_height  # 返回总路程和第 5 次反弹高度

# 输入处理
initial_height = float(input())
distance, height = ball_distance_and_height(initial_height)
print(round(distance, 6))  # 输出总路程，保留 6 位小数
print(round(height, 6))  # 输出第 5 次反弹高度，保留 6 位小数