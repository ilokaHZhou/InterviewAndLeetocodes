def train_sequences(trains):
    def dfs(stack, in_trains, out_trains):  # 深度优先搜索
        if not in_trains and not stack:  # 如果所有火车都已出站
            results.append(out_trains)  # 记录出站顺序
            return
        if in_trains:  # 如果还有火车未进站
            dfs(stack + [in_trains[0]], in_trains[1:], out_trains)  # 进站
        if stack:  # 如果站内有火车
            dfs(stack[:-1], in_trains, out_trains + [stack[-1]])  # 出站

    results = []  # 存储所有可能的出站顺序
    dfs([], trains, [])  # 调用深度优先搜索
    return sorted(results)  # 返回排序后的结果


# 输入处理
n = int(input())  # 火车数量
trains = list(map(int, input().split()))  # 火车进站顺序

# 调用函数并输出结果
sequences = train_sequences(trains)
for seq in sequences:
    print(" ".join(map(str, seq)))
