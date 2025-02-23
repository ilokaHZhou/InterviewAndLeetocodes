"""
1. 初始化边界：

    top 和 bottom 表示当前螺旋的上下边界。

    left 和 right 表示当前螺旋的左右边界。

2. 顺时针遍历：

    从左到右遍历顶部行：将顶部行的元素加入结果列表，然后上边界 top 下移。

    从上到下遍历右侧列：将右侧列的元素加入结果列表，然后右边界 right 左移。

    从右到左遍历底部行：如果上边界 top 仍小于等于下边界 bottom，则将底部行的元素加入结果列表，然后下边界 bottom 上移。

    从下到上遍历左侧列：如果左边界 left 仍小于等于右边界 right，则将左侧列的元素加入结果列表，然后左边界 left 右移。

3. 返回结果：

    最终返回存储所有元素的 result 列表。
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 从左到右遍历顶部行
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # 从上到下遍历右侧列
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # 从右到左遍历底部行
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # 从下到上遍历左侧列
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result