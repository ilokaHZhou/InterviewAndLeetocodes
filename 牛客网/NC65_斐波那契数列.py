# 要求输入一个正整数 n ，请你输出斐波那契数列的第 n 项。
# 空间复杂度O(1)和时间复杂度O(n)的解法
class Solution:
    def Fibonacci(self , n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr
    
"""
# 时间复杂度O(log(n))的解法
def matrix_mult(a, b):
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
    ]

def matrix_pow(mat, power):
    result = [[1, 0], [0, 1]]  # 单位矩阵
    while power > 0:
        if power % 2 == 1:
            result = matrix_mult(result, mat)
        mat = matrix_mult(mat, mat)
        power //= 2
    return result

def fibonacci_log_n(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    mat = [[1, 1], [1, 0]]
    result_mat = matrix_pow(mat, n - 1)
    return result_mat[0][0]

# 输入处理
n = int(input())
print(fibonacci_log_n(n))
"""