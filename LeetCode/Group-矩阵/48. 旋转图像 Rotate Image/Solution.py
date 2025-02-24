class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先转置矩阵，沿着左上到右下的轴转置
        for i in range(n):  # 遍历行
            for j in range(i, n):  # 遍历列，从对角线开始
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # 交换元素
        # 再翻转每一行
        for i in range(n):  # 遍历每一行
            matrix[i] = matrix[i][::-1]  # 反转行