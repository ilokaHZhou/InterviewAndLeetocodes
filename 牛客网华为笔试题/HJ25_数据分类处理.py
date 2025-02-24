def data_classification(I, R):
    R = sorted(set(R))  # 去重并排序
    result = []  # 存储最终结果

    for r in R:  # 遍历每个 R 中的元素
        r_str = str(r)
        matches = []  # 存储匹配的 I 的索引和值
        for idx, i in enumerate(I):  # 遍历 I 中的元素
            if r_str in str(i):  # 如果 R 的元素是 I 的元素的子串
                matches.append((idx, i))  # 记录匹配的索引和值
        if matches:  # 如果有匹配项
            result.append(r)  # 添加 R 的元素
            result.append(len(matches))  # 添加匹配项的数量
            for idx, i in matches:  # 添加匹配项的索引和值
                result.append(idx)
                result.append(i)

    # 输出结果
    print(len(result), end=" ")  # 输出结果的总长度
    print(" ".join(map(str, result)))  # 输出结果的具体内容


# 输入处理
I = list(map(int, input().split()[1:]))  # 读取 I 序列
R = list(map(int, input().split()[1:]))  # 读取 R 序列

# 调用函数
data_classification(I, R)
