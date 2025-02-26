# 读取输入的正整数 n
n = int(input())
# 初始化计数器，用于记录满足条件的数字个数
count = 0
# 遍历从 1 到 n 的所有数字
for i in range(1, n + 1):
    # 判断数字是否是 7 的倍数
    if i % 7 == 0:
        count += 1
    else:
        # 将数字转换为字符串，便于检查是否包含数字 7
        num_str = str(i)
        if "7" in num_str:
            count += 1
# 输出满足条件的数字个数
print(count)
