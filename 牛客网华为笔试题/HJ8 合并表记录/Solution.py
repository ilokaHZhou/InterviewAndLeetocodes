# 读取键值对的个数
n = int(input())

# 使用字典存储键值对
record_dict = {}

# 读取 n 行输入
for _ in range(n):
    key, value = map(int, input().split())
    if key in record_dict:
        record_dict[key] += value  # 如果键已存在，累加值
    else:
        record_dict[key] = value  # 如果键不存在，直接存储

# 按照键的升序排序并输出
for key in sorted(record_dict.keys()):
    print(key, record_dict[key])