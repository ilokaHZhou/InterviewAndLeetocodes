def calculate_operations(matrices, order):
    stack = []  # 用于存储矩阵的行列数
    total_ops = 0  # 总计算量
    for char in order:  # 遍历计算顺序
        if char == "(":  # 遇到左括号，跳过
            continue
        elif char == ")":  # 遇到右括号，计算栈顶两个矩阵的乘法
            if len(stack) < 2:  # 如果栈中不足两个矩阵
                continue
            # 弹出栈顶两个矩阵
            rows2, cols2 = stack.pop()
            rows1, cols1 = stack.pop()
            # 计算乘法次数并累加
            total_ops += rows1 * cols1 * cols2
            # 将结果矩阵的行列数压入栈
            stack.append((rows1, cols2))
        else:  # 遇到矩阵，将其行列数压入栈
            idx = ord(char) - ord("A")  # 将字母转换为索引
            stack.append(matrices[idx])
    return total_ops  # 返回总计算量


# 输入处理
n = int(input())  # 矩阵个数
matrices = []
for _ in range(n):
    rows, cols = map(int, input().split())
    matrices.append((rows, cols))  # 存储矩阵的行列数
order = input().strip()  # 计算顺序

# 调用函数并输出结果
print(calculate_operations(matrices, order))
