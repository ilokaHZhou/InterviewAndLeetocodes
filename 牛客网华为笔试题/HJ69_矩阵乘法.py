def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])  # 矩阵 A 的行数和列数
    rows_B, cols_B = len(B), len(B[0])  # 矩阵 B 的行数和列数
    if cols_A != rows_B:  # 检查矩阵是否可以相乘
        return None
    # 初始化结果矩阵
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):  # 遍历 A 的行
        for j in range(cols_B):  # 遍历 B 的列
            for k in range(cols_A):  # 计算点积
                result[i][j] += A[i][k] * B[k][j]
    return result  # 返回结果矩阵


# 输入处理
x = int(input())  # 矩阵 A 的行数
y = int(input())  # 矩阵 A 的列数（矩阵 B 的行数）
z = int(input())  # 矩阵 B 的列数
A = [list(map(int, input().split())) for _ in range(x)]  # 输入矩阵 A
B = [list(map(int, input().split())) for _ in range(y)]  # 输入矩阵 B

# 调用函数并输出结果
result = matrix_multiply(A, B)
for row in result:
    print(" ".join(map(str, row)))
