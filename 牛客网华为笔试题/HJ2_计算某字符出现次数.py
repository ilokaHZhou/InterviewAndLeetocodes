# 读取输入字符串
s = input().strip()

# 读取目标字符
target_char = input().strip()

# 统一转换为大写（或小写），不区分大小写
s_upper = s.upper()
target_char_upper = target_char.upper()

# 统计目标字符出现的次数
count = s_upper.count(target_char_upper)
print(count)