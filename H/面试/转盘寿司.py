# 读取一行输入，按空格分割，然后将每个数字字符串转换为整数，并收集到列表中
prices = list(map(int, input().split()))
# 获取寿司价格列表的长度，代表寿司盘数
n = len(prices)

# 创建一个列表来存储结果，即每个寿司盘享受优惠后的总价格
res = [0] * n
# 创建一个列表作为栈使用，用于跟踪寿司价格的索引
stack = []

# 遍历每个寿司盘的价格，由于寿司盘是循环的，需要遍历两倍长度减一次
for j in range(n * 2 - 1):
    # 计算当前索引，由于列表是循环的，使用模运算得到实际索引
    index = j % n
    # 当栈不为空且栈顶元素的价格大于当前索引对应的价格时
    while stack and prices[stack[-1]] > prices[index]:
        # 弹出栈顶元素的索引
        top_index = stack.pop()
        # 计算栈顶元素享受优惠后的价格，并更新结果列表
        res[top_index] = prices[top_index] + prices[index]
    # 第一轮遍历时，将索引压入栈中
    if j < n:
        stack.append(index)

# 遍历完成后，栈中剩余的元素代表它们右侧没有更小的价格
# 直接将它们自身的价格作为结果
while stack:
    top_index = stack.pop()
    res[top_index] = prices[top_index]

# 输出结果，每个价格后加上空格
print(' '.join(map(str, res)))
