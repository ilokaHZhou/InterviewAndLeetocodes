priority_list = list(map(int, input().split(',')))

# 创建任务列表，每个任务用 (原始索引, 优先级) 表示
task_list = [(i, priority_list[i]) for i in range(len(priority_list))]

# 按照任务的优先级从大到小排序，优先级高的排在前面
task_list.sort(key=lambda x: -x[1])

# 初始化当前任务索引，记录打印顺序
current_task = 0
print_order = []

# 遍历任务列表，按照当前任务的原始索引找到其在排序后的位置
while current_task < len(task_list):
    for i in range(len(task_list)):
        if task_list[i][0] == current_task:  # 如果找到原始索引等于当前任务
            print_order.append(i)  # 记录排序后的任务位置
    current_task += 1  # 处理下一个任务

# 将打印顺序列表转换为逗号分隔的字符串输出
print(','.join(map(str, print_order)))