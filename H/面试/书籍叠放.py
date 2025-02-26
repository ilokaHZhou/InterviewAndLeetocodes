import sys   
import bisect   

# 读取用户输入的书籍数据，假设输入形如 [[20,16],[21,15],[22,14]]
books = eval(input())  # eval 将输入的字符串转化为实际的 Python 数据结构（二维列表）

# 对书籍列表按照书的长度从小到大排序，如果长度相同则按照宽度从大到小排序
books.sort(key=lambda x: (x[0], -x[1]))  
# lambda 函数 x[0] 表示按长度排序，x[1] 前面的负号表示宽度按照降序排列

# 提取所有书籍的宽度，生成一个列表
widths = list(map(lambda x: x[1], books))  # 使用 map 提取每本书的宽度并转换为列表

# 初始化最长不下降子序列（LIS），首先将第一个宽度值放入 LIS 列表
lis = [widths[0]]

# 遍历所有书籍的宽度，从第二本书开始
for i in range(1, len(widths)):
    # 如果当前书的宽度大于 LIS 列表中的最后一个元素，则将其追加到 LIS 中
    if widths[i] > lis[-1]:
        lis.append(widths[i])
    # 如果当前书的宽度小于 LIS 列表中的第一个元素，替换第一个元素
    elif widths[i] < lis[0]:
        lis[0] = widths[i]
    # 否则，使用二分查找找到第一个大于或等于当前宽度的位置，并替换它
    else:
        idx = bisect.bisect_left(lis, widths[i])
        lis[idx] = widths[i]

# 输出 LIS 的长度，即可以叠放的最多书籍数量
print(len(lis))