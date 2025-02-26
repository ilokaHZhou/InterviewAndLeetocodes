from collections import deque

# 定义一个类表示网格中的一个单元格
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

# 使用广度优先搜索（BFS）检查是否存在一条从起点到终点的路径
# 路径上所有单元格的信号质量都不低于minSignal
def bfs(Cov, minSignal):
    R, C = len(Cov), len(Cov[0])
    # 如果起点或终点的信号质量低于minSignal，直接返回false
    if Cov[0][0] < minSignal or Cov[R - 1][C - 1] < minSignal:
        return False

    # visited数组用于记录哪些单元格已经被访问过，避免重复访问
    visited = [[False for _ in range(C)] for _ in range(R)]
    queue = deque()
    queue.append(Cell(0, 0))
    visited[0][0] = True

    # dr和dc数组用于表示从当前单元格向四个方向（上下左右）移动的行和列的变化量
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue:
        cell = queue.popleft()
        # 如果到达终点，返回True
        if cell.row == R - 1 and cell.col == C - 1:
            return True

        # 否则，尝试向四个方向移动
        for i in range(4):
            nr, nc = cell.row + dr[i], cell.col + dc[i]

            # 如果新的单元格在网格内，且没有被访问过，且信号质量不低于minSignal，将其加入队列并标记为已访问
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and Cov[nr][nc] >= minSignal:
                queue.append(Cell(nr, nc))
                visited[nr][nc] = True

    # 如果没有找到有效路径，返回False
    return False

# 使用二分搜索找到最大的满足条件的信号质量
def binary_search(Cov, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        # 如果存在一条有效路径，尝试更高的信号质量
        if bfs(Cov, mid):
            low = mid + 1
        else:  # 否则，降低信号质量
            high = mid - 1
    # 返回最大的满足条件的信号质量
    return high

# 主函数
def main():
    R = int(input())
    C = int(input())
    Cov = [list(map(int, input().split())) for _ in range(R)]

    minSignal = min(min(row) for row in Cov)
    maxSignal = max(max(row) for row in Cov)

    # 输出最大的满足条件的信号质量
    print(binary_search(Cov, minSignal, maxSignal))

if __name__ == "__main__":
    main()