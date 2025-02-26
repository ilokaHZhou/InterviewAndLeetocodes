# 输入获取，读入网格地图大小、地图数据和目标位置
num_rows, num_cols = map(int, input().split())
grid_map = list(map(int, input().split()))
target_pos = list(map(int, input().split()))

# 算法入口
def get_signal_strength(map_array, num_rows, num_cols, target_pos):
    # 初始化队列，将所有信号源位置加入队列
    queue = [[i, j] for j in range(num_cols) for i in range(num_rows) if map_array[i*num_cols+j] > 0]
    # 定义四个方向偏移量
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # 广度优先搜索
    while queue:
        new_queue = []
        for i, j in queue:
            signal_strength = map_array[i*num_cols+j] - 1  # 计算信号强度
            for dx, dy in directions:
                new_i, new_j = i+dx, j+dy  # 计算新位置
                if 0 <= new_i < num_rows and 0 <= new_j < num_cols and map_array[new_i*num_cols+new_j] == 0:
                    # 如果新位置在地图内且为空旷位置，则更新该位置信号强度并将其加入队列
                    map_array[new_i*num_cols+new_j] = signal_strength
                    new_queue.append([new_i, new_j])
        queue = new_queue
        
    # 返回目标位置的信号强度（如果未被覆盖到则返回0）
    target_row, target_col = target_pos
    return max(0, map_array[target_row*num_cols+target_col])

# 算法调用，输出结果
print(get_signal_strength(grid_map, num_rows, num_cols, target_pos))