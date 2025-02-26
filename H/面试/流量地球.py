def has_inactive_engines(engine_statuses):
    """检查列表中是否有引擎处于未激活状态（即状态为 -1）。
    返回值为布尔类型，True表示存在未激活的引擎，False则表示所有引擎均已激活。"""
    return -1 in engine_statuses

def activate_adjacent_engines(engine_statuses, current_engine, activation_time, total_engines):
    """激活指定引擎的相邻引擎。计算并更新左右两边的引擎状态。
    - current_engine: 当前引擎的索引。
    - activation_time: 当前引擎的激活时间。
    - total_engines: 引擎总数，用于计算边界条件。"""
    left_engine = total_engines - 1 if current_engine == 0 else current_engine - 1
    right_engine = 0 if current_engine == total_engines - 1 else current_engine + 1
    if engine_statuses[left_engine] == -1:
        engine_statuses[left_engine] = activation_time
    if engine_statuses[right_engine] == -1:
        engine_statuses[right_engine] = activation_time

def update_engine_statuses(engine_statuses, start_time):
    """更新所有引擎的激活状态，直到所有引擎都被激活。
    进行循环检查，若当前时间点有引擎被激活，则激活其相邻引擎，并递增时间步长。"""
    continue_update = True
    while continue_update:
        for i, status in enumerate(engine_statuses):
            if status == start_time:        
                activate_adjacent_engines(engine_statuses, i, start_time + 1, len(engine_statuses))
        start_time += 1
        continue_update = has_inactive_engines(engine_statuses)
    last_activation_time = max(engine_statuses)
    count_active_engines = sum(status == last_activation_time for status in engine_statuses)
    engines_report = ' '.join(str(i) for i, status in enumerate(engine_statuses) if status == last_activation_time)
    print(count_active_engines)  # 打印在最后一个激活时间被激活的引擎数量
    print(engines_report.strip())  # 打印这些引擎的索引

# 主循环，持续接受输入直到遇到文件结束符（EOF）
while True:
    try:
        inputs = input().split()
        number_of_engines = int(inputs[0])  # 读取引擎总数
        number_of_entries = int(inputs[1])  # 读取条目数量

        engine_statuses = [-1] * number_of_engines  # 初始化引擎状态数组，初始值为-1表示未激活
        earliest_activation = float('inf')  # 设置最早激活时间为无穷大

        for _ in range(number_of_entries):
            time_index = input().split()
            activation_time = int(time_index[0])
            engine_index = int(time_index[1])
            engine_statuses[engine_index] = activation_time  # 更新指定引擎的激活时间
            earliest_activation = min(earliest_activation, activation_time)  # 更新最早激活时间

        update_engine_statuses(engine_statuses, earliest_activation)  # 根据最早激活时间更新引擎状态
    except EOFError:
        break  # 结束循环，等待输入结束