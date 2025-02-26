# 导入必要的库
from collections import defaultdict, deque
 
    

def calc_total_income(parent_id, parent_to_children, income):
    """
    使用递归的深度优先搜索算法计算分销商的总收入，包括从下级分销商获取的部分
    """
    # 获取当前父分销商的子分销商列表
    children = parent_to_children[parent_id]

    # 如果该父分销商有子分销商
    if children:
        # 遍历所有子分销商
        for child_id in children:
            # 递归计算子分销商的总收入
            calc_total_income(child_id, parent_to_children, income)
            # 计算父分销商从该子分销商处获取的提成收入
            additional_income = income[child_id] // 100 * 15
            # 将提成收入累加到父分销商的总收入中
            income[parent_id] += additional_income

# 读取输入的分销关系数量
n = int(input().strip())

# 记录每个分销商的收入
income = {}
# 记录所有的分销商 ID
ids = set()
# 记录子分销商到父分销商的映射关系
child_to_parent = {}
# 记录父分销商到其所有子分销商的映射关系
parent_to_children = defaultdict(list)

# 读取输入数据并构建映射关系
for _ in range(n):
    # 读取当前行并按空格分割
    parts = input().strip().split()
    # 解析当前子分销商的 ID
    child_id = int(parts[0])
    # 解析当前子分销商的父分销商 ID
    parent_id = int(parts[1])
    # 解析当前子分销商的收入
    child_income = int(parts[2])

    # 将子分销商的收入记录在 income 映射中
    income[child_id] = child_income
    # 将子分销商和父分销商的 ID 添加到分销商 ID 集合中
    ids.add(child_id)
    ids.add(parent_id)

    # 记录子分销商到父分销商的映射关系
    child_to_parent[child_id] = parent_id

    # 如果父分销商还没有子分销商列表，则初始化一个新的列表（由 defaultdict 自动处理）
    # 将当前子分销商 ID 添加到父分销商的子分销商列表中
    parent_to_children[parent_id].append(child_id)

# 寻找顶级分销商 (即没有父分销商的分销商，即 boss)
for id in ids:
    # 如果当前分销商 ID 不在 child_to_parent 映射中，说明它是顶级分销商
    if id not in child_to_parent:
        # 初始化顶级分销商的收入为 0，因为它自身没有任何直接收入
        income[id] = 0
        # 调用深度优先搜索算法计算该顶级分销商的总收入（包括来自下级分销商的提成）
        calc_total_income(id, parent_to_children, income)
        # 输出顶级分销商的 ID 和其计算出的总收入
        print(f"{id} {income[id]}")
        # 一旦找到顶级分销商，结束循环
        break 