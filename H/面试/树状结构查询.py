n = int(input())  # 输入行数

tree = {}  # 创建一个字典用于存储树的关系

# 读取输入的树的关系，并将子节点和父节点存入字典中
for _ in range(n):
    childNode, parentNode = input().split()  # 子节点和父节点

    if parentNode not in tree:
        tree[parentNode] = set()  # 如果父节点不在字典中，则创建一个空集合

    tree[parentNode].add(childNode)  # 将子节点添加到父节点的集合中

targetNode = input()  # 输入要查询的节点

if targetNode not in tree:  # 如果字典中不包含要查询的节点，则输出空行并结束程序
    print("")
    exit()

queue = list(tree[targetNode])  # 创建一个队列，用于存储要遍历的节点

result = []  # 创建一个列表，用于存储查询节点的所有下层节点

# 遍历队列，将节点添加到结果集中，并将该节点的子节点添加到队列中
while queue:
    node = queue.pop(0)  # 从队列中取出节点
    result.append(node)  # 将节点添加到结果集中

    if node in tree:  # 如果节点在字典中有子节点，则将子节点添加到队列中
        queue.extend(tree[node])

result.sort()  # 对结果集进行排序

for node in result:  # 打印结果集中的每个节点
    print(node)