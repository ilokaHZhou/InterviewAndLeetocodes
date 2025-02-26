# 处理输入
itemNumber = int(input())  # 商品数量
days = int(input())  # 售货天数

maxItems = list(map(int, input().split()))  # 每件商品最大持有数量

prices = [list(map(int, input().split())) for _ in range(itemNumber)]  # 商品价格列表

# 贪心算法
maxProfit = 0
for i in range(itemNumber):  # 遍历每件商品
    for j in range(1, days):  # 遍历商品价格列表，求出每天的利润
        profit = max(0, prices[i][j] - prices[i][j - 1])
        # 当前价格减去前一天价格，如果为负数则代表亏本，不计入利润
        maxProfit += profit * maxItems[i]  # 求出当前商品能够获取的最大利润

print(maxProfit)  # 输出最大利润