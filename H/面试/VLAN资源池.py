import sys

# 输入VLAN资源池
vlan_pool_input = input()
# 输入业务要申请的VLAN
dest_vlan = int(input())

# 定义存储VLAN的列表
vlan_pool = []

# 将输入的VLAN资源池按逗号分隔为多个VLAN组
vlan_group = vlan_pool_input.split(",")

# 遍历每个VLAN组
for vlan_item in vlan_group:
    # 如果VLAN组中包含连续的VLAN
    if "-" in vlan_item:
        # 将连续的VLAN拆分为开始VLAN和结束VLAN
        vlan_items = vlan_item.split("-")
        start_vlan = int(vlan_items[0])
        end_vlan = int(vlan_items[1])
        # 将连续的VLAN添加到VLAN资源池中
        for j in range(start_vlan, end_vlan + 1):
            vlan_pool.append(j)
        continue
    # 如果VLAN组中只有一个VLAN
    vlan_pool.append(int(vlan_item))

# 对VLAN资源池进行升序排序
vlan_pool.sort()

# 如果申请的VLAN在VLAN资源池中
if dest_vlan in vlan_pool:
    # 从VLAN资源池中移除申请的VLAN
    vlan_pool.remove(dest_vlan)

# 定义存储结果的列表
result = []
# 定义上一个VLAN的变量
last_vlan = None

# 遍历VLAN资源池中的每个VLAN
for index in range(len(vlan_pool)):
    # 如果是第一个VLAN
    if last_vlan is None:
        result.append(str(vlan_pool[index]))
        last_vlan = vlan_pool[index]
        continue
    # 如果当前VLAN与上一个VLAN连续
    if vlan_pool[index] - last_vlan == 1:
        # 如果结果列表中的最后一个元素以"-上一个VLAN"结尾
        if result[-1].endswith("-" + str(last_vlan)):
            # 将结果列表中的最后一个元素更新为"-当前VLAN"
            result[-1] = result[-1][:result[-1].rindex(str(last_vlan))] + str(vlan_pool[index])
        else:
            # 在结果列表中添加"-当前VLAN"
            result.append("-" + str(vlan_pool[index]))
    else:
        # 在结果列表中添加",当前VLAN"
        result.append("," + str(vlan_pool[index]))
    last_vlan = vlan_pool[index]

# 输出结果列表中的VLAN资源池
print("".join(result))