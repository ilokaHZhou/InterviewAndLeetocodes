class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []  # 初始化杨辉三角
        for row_num in range(numRows):  # 遍历每一行
            row = [1] * (row_num + 1)  # 初始化当前行，全部赋值为 1
            for j in range(1, row_num):  # 计算中间每个位置的值
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]  # 状态转移方程
            triangle.append(row)  # 将当前行添加到杨辉三角
        return triangle  # 返回杨辉三角

