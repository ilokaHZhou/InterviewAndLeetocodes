class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(n, h, pairs):  # 根据输入规则构建链表
    head = ListNode(h)  # 创建头节点
    node_map = {h: head}  # 存储节点值对应的节点对象
    for i in range(0, len(pairs), 2):  # 遍历插入规则
        a, b = pairs[i], pairs[i + 1]  # 提取插入规则 (a, b)
        if b not in node_map:  # 如果 b 节点不存在
            continue
        new_node = ListNode(a)  # 创建新节点
        node_map[a] = new_node  # 存储新节点
        # 将新节点插入到 b 节点后
        new_node.next = node_map[b].next
        node_map[b].next = new_node
    return head  # 返回链表头节点

def delete_node(head, target):  # 删除指定值的节点
    dummy = ListNode(0, head)  # 虚拟头节点
    current = dummy
    while current.next:  # 遍历链表
        if current.next.val == target:  # 找到目标节点
            current.next = current.next.next  # 删除节点
        else:
            current = current.next
    return dummy.next  # 返回链表头节点

# 输入处理
data = list(map(int, input().split()))  # 读取输入
n = data[0]  # 节点总数
h = data[1]  # 头节点的值
pairs = data[2:-1]  # 插入规则
target = data[-1]  # 目标节点值

# 构建链表并删除目标节点
head = build_linked_list(n, h, pairs)
head = delete_node(head, target)

# 输出结果
result = []
while head:
    result.append(str(head.val))
    head = head.next
print(" ".join(result))