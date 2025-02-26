from collections import OrderedDict

# 创建函数用于读取输入
def read_input():
    return input().strip()

# 读取顾客数量
n = int(read_input())

# 使用 OrderedDict 存储订单时间，保证有序
order_time = OrderedDict()

# 读取顾客订单时间并存入 OrderedDict
for _ in range(n):
    time = read_input()
    # 将订单时间作为键，值为该时间出现的次数
    order_time[time] = order_time.get(time, 0) + 1

# 初始化免单顾客数量
free_orders = 0
# 用于存储上一个订单的秒数
prev_second = ""

# 遍历 OrderedDict 中的订单时间
for time, count in order_time.items():
    # 获取当前订单时间的秒数
    current_second = time[:19]
    # 如果当前订单秒数与上一个订单秒数不同，则将当前订单的数量加入免单顾客数
    if current_second != prev_second:
        free_orders += count
        prev_second = current_second

# 输出免单顾客数量
print(free_orders)