# 使用字典模拟链表
node_map = {}

# 读取输入
head_address, n = input().split()
n = int(n)

# 读取每个节点的信息并存储在字典中
for _ in range(n):
    address, value, next_address = input().split()
    node_map[address] = (value, next_address)


# 初始化慢指针和快指针，均指向头节点
slow = head_address
fast = head_address

# 快指针每次走两步，慢指针每次走一步，直到快指针到达链表末尾
while fast != '-1' and fast in node_map:
    fast = node_map[fast][1]  # 快指针走一步
    if fast == '-1' or fast not in node_map:
        break  # 快指针到达链表末尾，结束循环
    fast = node_map[fast][1]  # 快指针再走一步
    slow = node_map[slow][1]  # 慢指针走一步

# 输出慢指针指向的节点的值
print(node_map[slow][0])