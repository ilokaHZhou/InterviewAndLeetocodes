import heapq

# 定义Node类，用于构建哈夫曼树的节点
class Node:
    def __init__(self, value):
        self.value = value  # 节点存储的数值
        self.left = None  # 节点的左子节点
        self.right = None  # 节点的右子节点
        self.height = 0  # 节点的高度

    # 重载小于操作符，用于优先队列中比较Node对象
    def __lt__(self, other):
        # 首先比较节点的权值，如果权值相同，则比较高度
        if self.value == other.value:
            return self.height < other.height
        return self.value < other.value

# 构建哈夫曼树的函数
def build_huffman_tree(values):
    pq = [Node(value) for value in values]  # 创建Node对象列表
    heapq.heapify(pq)  # 将列表转换为最小堆
    while len(pq) > 1:  # 当堆中有多于一个节点时
        left = heapq.heappop(pq)  # 弹出两个数值最小的节点
        right = heapq.heappop(pq)
        parent = Node(left.value + right.value)  # 创建新节点，其数值为两个子节点数值之和
        parent.left = left  # 设置新节点的左子节点
        parent.right = right  # 设置新节点的右子节点
        parent.height = max(left.height, right.height) + 1  # 更新节点的高度
        heapq.heappush(pq, parent)  # 将新节点加入堆中
    return pq[0]  # 返回堆中剩下的最后一个节点，即哈夫曼树的根节点

# 中序遍历哈夫曼树的函数
def inorder_traversal(root):
    if root is not None:  # 如果当前节点不为空
        yield from inorder_traversal(root.left)  # 递归遍历左子树
        yield root.value  # 返回当前节点的值
        yield from inorder_traversal(root.right)  # 递归遍历右子树
 
n = int(input())  # 从标准输入读取数字的个数
values = list(map(int, input().split()))  # 从标准输入读取数字，并转换为整数列表
root = build_huffman_tree(values)  # 构建哈夫曼树，并获取根节点
result = ' '.join(map(str, inorder_traversal(root)))  # 对哈夫曼树进行中序遍历，并将结果转换为字符串
print(result)  # 打印中序遍历的结果
