from collections import defaultdict

# 定义一个常量数组，表示上下左右四个方向的偏移量
OFFSETS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

# 深度优先搜索函数
def dfs(x, y, step, min_step_to_height, matrix, m, n, k, memo, visited):
    # 获取当前位置的高度
    last_height = matrix[x][y]

    # 遍历四个方向
    for offset in OFFSETS:
        # 计算新的位置
        new_x = x + offset[0]
        new_y = y + offset[1]

        # 检查新位置是否在矩阵范围内
        if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
            continue

        # 获取新位置的高度
        cur_height = matrix[new_x][new_y]

        # 检查两个位置的高度差是否在k以内
        if abs(cur_height - last_height) <= k:
            # 增加步数
            step += 1

            # 更新到达新高度的最短步数
            if cur_height not in min_step_to_height or min_step_to_height[cur_height] > step:
                min_step_to_height[cur_height] = step

            # 检查记忆化数组，避免重复计算
            if memo[new_x][new_y] == 0 or memo[new_x][new_y] > step:
                # 更新记忆化数组
                memo[new_x][new_y] = step
                # 标记当前位置为已访问
                visited[x][y] = True

                # 递归调用深度优先搜索
                dfs(new_x, new_y, step, min_step_to_height, matrix, m, n, k, memo, visited)

                # 回溯时，将当前位置标记为未访问
                visited[x][y] = False

            # 减少步数
            step -= 1

# 主函数
def main():
    # 读取输入的m, n, k
    m, n, k = map(int, input().split())
    # 初始化山地图矩阵
    matrix = [list(map(int, input().split())) for _ in range(m)]

    # 初始化一个哈希表，用于存储到达不同高度的最短步数
    min_step_to_height = {matrix[0][0]: 0}
    # 初始化一个记忆化数组，用于记录已经访问过的位置和步数
    memo = [[0] * n for _ in range(m)]
    # 初始化一个布尔数组，用于记录已经访问过的位置
    visited = [[False] * n for _ in range(m)]

    # 调用深度优先搜索函数
    dfs(0, 0, 0, min_step_to_height, matrix, m, n, k, memo, visited)

    # 计算最高峰的高度和最短步数
    max_height = max(min_step_to_height.keys())
    min_step = min_step_to_height[max_height]

    # 输出结果
    print(max_height, min_step)

# 程序入口
if __name__ == "__main__":
    main()