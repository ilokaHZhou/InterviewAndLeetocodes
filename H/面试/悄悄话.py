from collections import deque

# 读取一行输入并将其转换为整数列表
# 列表中的每个元素代表从父节点到当前节点的时间
whisper_times = list(map(int, input().split()))

# 记录最后一个节点接收悄悄话的时间
max_time = 0

# 使用队列来进行二叉树的层次遍历
node_queue = deque([0])  # 将根节点索引0加入队列

# 当队列不为空时，继续遍历
while node_queue:
    # 从队列中取出一个节点索引
    parent_node_index = node_queue.popleft()

    # 计算左子节点索引
    left_child_index = 2 * parent_node_index + 1
    # 计算右子节点索引
    right_child_index = 2 * parent_node_index + 2

    # 如果左子节点存在，处理左子节点
    if left_child_index < len(whisper_times) and whisper_times[left_child_index] != -1:
        # 更新左子节点的时间（父节点时间 + 当前节点时间）
        whisper_times[left_child_index] += whisper_times[parent_node_index]
        # 将左子节点加入队列
        node_queue.append(left_child_index)
        # 更新最大时间
        max_time = max(max_time, whisper_times[left_child_index])

    # 如果右子节点存在，处理右子节点
    if right_child_index < len(whisper_times) and whisper_times[right_child_index] != -1:
        # 更新右子节点的时间（父节点时间 + 当前节点时间）
        whisper_times[right_child_index] += whisper_times[parent_node_index]
        # 将右子节点加入队列
        node_queue.append(right_child_index)
        # 更新最大时间
        max_time = max(max_time, whisper_times[right_child_index])

# 所有节点都接收到悄悄话后，打印最大时间
print(max_time)