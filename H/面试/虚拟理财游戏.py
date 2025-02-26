import sys

# 读取一行输入并将其转换为整数列表的函数
def read_int_array():
    # 使用input()替换sys.stdin.readline()以适应在线编译器
    return list(map(int, input().split()))

# 读取投资项目数量m、总投资额N和风险容忍度X
m, N, X = read_int_array()
# 读取每个项目的预期回报率
returns = read_int_array()
# 读取每个项目的风险值
risks = read_int_array()
# 读取每个项目的最大投资额
max_investments = read_int_array()

# 初始化最大回报为0
max_return = 0
# 初始化最大回报对应的投资方案列表
best_investments = [0] * m

# 遍历所有项目
for i in range(m):
    # 检查项目i的风险是否在容忍度X以内
    if risks[i] <= X:
        # 计算项目i的投资额，不超过总投资额N和项目i的最大投资额
        investment_for_i = min(N, max_investments[i])
        # 计算当前项目的回报
        current_return = investment_for_i * returns[i]
        # 如果当前回报大于已知的最大回报
        if current_return > max_return:
            # 更新最大回报
            max_return = current_return
            # 重置最佳投资方案列表，并为项目i分配投资额
            best_investments = [0] * m
            best_investments[i] = investment_for_i

    # 遍历项目i之后的项目，寻找两个项目的组合投资方案
    for j in range(i + 1, m):
        # 如果两个项目的风险总和在容忍度范围内
        if risks[i] + risks[j] <= X:
            # 根据预期回报率决定投资额分配
            if returns[i] > returns[j]:
                # 如果项目i的回报率高于项目j，优先投资项目i
                investment_for_i = min(N, max_investments[i])
                # 计算项目j的剩余可投资额
                investment_for_j = min(N - investment_for_i, max_investments[j])
            else:
                # 如果项目j的回报率高于项目i，优先投资项目j
                investment_for_j = min(N, max_investments[j])
                # 计算项目i的剩余可投资额
                investment_for_i = min(N - investment_for_j, max_investments[i])
            # 计算两个项目组合的当前回报
            current_return = investment_for_i * returns[i] + investment_for_j * returns[j]
            # 如果当前回报大于已知的最大回报
            if current_return > max_return:
                # 更新最大回报
                max_return = current_return
                # 重置最佳投资方案列表，并为两个项目分配投资额
                best_investments = [0] * m
                best_investments[i] = investment_for_i
                best_investments[j] = investment_for_j

# 输出最佳投资方案
print(' '.join(map(str, best_investments)))