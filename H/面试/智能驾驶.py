import heapq

# 定义常量，表示汽车油箱的最大容量
MAX_FUEL = 100

def main():
    # 从标准输入读取行数和列数，并以逗号分隔
    numRows, numCols = map(int, input().split(","))
    # 读取地图数据，每一行通过逗号分隔，对于每行输入，读取numRows行
    map_data = [list(map(int, input().split(","))) for _ in range(numRows)]

    # 计算并获取最小初始油量
    min_fuel = find_minimum_initial_fuel(map_data, numRows, numCols)
    # 输出计算得到的最小初始油量
    print(min_fuel)

def find_minimum_initial_fuel(map_data, numRows, numCols):
    # 初始化二分查找的边界
    low, high = 0, MAX_FUEL
    optimal_fuel = -1  # 最优的油量值，默认为-1表示未找到

    # 二分查找确定合适的起始油量
    while low <= high:
        mid = (low + high) // 2
        # 检查中值油量是否可以从起点到达终点
        if can_reach_destination(map_data, mid, numRows, numCols):
            optimal_fuel = mid  # 更新找到的最小可行油量
            high = mid - 1  # 尝试更小的油量
        else:
            low = mid + 1  # 增加油量尝试
    
    return optimal_fuel

def can_reach_destination(map_data, start_fuel, numRows, numCols):
    # 如果起点是障碍物，则无法出发
    if map_data[0][0] == 0:
        return False

    # 初始化存储每个单元格剩余油量的二维列表
    remaining_fuel = [[-1 for _ in range(numCols)] for _ in range(numRows)]
    # 设置起点的初始油量，考虑起点可能为负值消耗的情况
    remaining_fuel[0][0] = MAX_FUEL if map_data[0][0] == -1 else start_fuel - map_data[0][0]
    if remaining_fuel[0][0] < 0:
        return False  # 起始油量不足以离开起点

    # 使用优先队列，以最大剩余油量优先处理
    priority_queue = []
    heapq.heappush(priority_queue, (-remaining_fuel[0][0], 0, 0))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 定义上下左右四个方向

    # 使用优先队列执行BFS
    while priority_queue:
        current_fuel, current_row, current_col = heapq.heappop(priority_queue)
        current_fuel = -current_fuel  # 因为用了负值来实现最大堆
        
        # 到达终点检查
        if current_row == numRows - 1 and current_col == numCols - 1:
            return True
        
        # 检查四个可能的移动方向
        for dx, dy in directions:
            new_row, new_col = current_row + dx, current_col + dy
            if is_valid(new_row, new_col, numRows, numCols, map_data):
                new_fuel = MAX_FUEL if map_data[new_row][new_col] == -1 else current_fuel - map_data[new_row][new_col]
                if new_fuel > remaining_fuel[new_row][new_col]:
                    remaining_fuel[new_row][new_col] = new_fuel
                    heapq.heappush(priority_queue, (-new_fuel, new_row, new_col))
                    
    return False  # 如果没有找到到达终点的路径则返回False

def is_valid(row, col, numRows, numCols, map_data):
    # 检查位置是否有效（不越界且不是障碍物）
    return 0 <= row < numRows and 0 <= col < numCols and map_data[row][col] != 0

if __name__ == "__main__":
    main()