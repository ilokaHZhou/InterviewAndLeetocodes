import sys

# 读取商品价格输入并用逗号分割
goods_input = input().split(",")
# 将输入的商品价格转换为整数列表
goods = [int(x) for x in goods_input]
# 读取预算金额
max_money = int(input())
# 用于存储满足条件的总价
res = []

# 三重循环遍历所有可能的三件商品组合
for i in range(len(goods) - 2):
    for j in range(i + 1, len(goods) - 1):
        for k in range(j + 1, len(goods)):
            # 计算当前三件商品的总价
            tmp = goods[i] + goods[j] + goods[k]
            # 如果总价不超过预算，则加入结果列表
            if tmp <= max_money:
                res.append(tmp)

# 检查结果列表是否为空
if len(res) > 0:
    # 找到结果列表中的最大总价
    max = res[0]
    for i in range(1, len(res)):
        if res[i] > max:
            max = res[i]
    # 输出最大总价
    print(max)
else:
    # 如果没有找到满足条件的组合，输出 -1
    print(-1)