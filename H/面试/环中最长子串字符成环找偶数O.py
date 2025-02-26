# 读取用户输入的字符串
input_str = input("")
# 获取字符串的长度
len_str = len(input_str)
# 初始化'o'字符的计数器
num = 0
# 遍历字符串，统计'o'字符的数量
for chr in input_str:
    if chr == 'o':
        num += 1
# 如果'o'字符出现的次数是偶数，则输出字符串的长度
if num % 2 == 0:
    print(len_str)
else:
    # 如果'o'字符出现的次数是奇数，则输出字符串长度减1
    print(len_str - 1)
