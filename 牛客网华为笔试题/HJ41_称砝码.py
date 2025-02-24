def count_possible_weights(n, weights, counts):
    # 所有可能的重量组合
    possible_weights = {0}
    for i in range(n):
        weight = weights[i]
        count = counts[i]
        # 遍历当前已有的重量组合
        current_weights = list(possible_weights)
        for w in current_weights:
            # 为每个已有重量添加新砝码的重量组合
            for k in range(1, count + 1):
                possible_weights.add(w + k * weight)
    return len(possible_weights)


# 输入处理
n = int(input())
weights = list(map(int, input().split()))
counts = list(map(int, input().split()))

# 输出结果
print(count_possible_weights(n, weights, counts))
