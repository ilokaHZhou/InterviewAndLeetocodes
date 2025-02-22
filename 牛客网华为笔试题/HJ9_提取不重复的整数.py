# 读取输入整数
n = input().strip()

# 从右往左提取不重复的数字
seen = set()
result = []
for char in reversed(n):
    if char not in seen:
        seen.add(char)
        result.append(char)

# 输出结果
print(''.join(result))