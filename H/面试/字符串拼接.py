# 导入所需的模块
from collections import defaultdict

# 递归生成满足条件的不同字符串
def generate_distinct_strings(s, length, current, result, used):
    # 当生成的字符串长度等于指定长度时，将其加入到结果集中
    if len(current) == length:
        result.add(current)
        return

    # 遍历字符串中的字符
    for i in range(len(s)):
        # 判断字符是否已经被使用，或者当前字符与前一个字符相同
        if used[i] or (len(current) > 0 and current[-1] == s[i]):
            continue  # 如果字符已被使用或与前一个字符相同，则跳过当前字符
        used[i] = True  # 标记当前字符为已使用
        # 递归调用生成下一个字符
        generate_distinct_strings(s, length, current + s[i], result, used)
        used[i] = False  # 取消标记当前字符的使用状态，以便下一次遍历

# 计算满足条件的不同字符串的数量
def count_distinct_strings(s, length):
    # 创建一个集合来存储不同的字符串
    distinct_strings = set()
    # 创建一个列表来标记字符串中的字符是否已经被使用
    used = [False] * len(s)
    # 调用generate_distinct_strings方法生成满足条件的不同字符串
    generate_distinct_strings(s, length, "", distinct_strings, used)
    # 打印生成的所有不同的字符串
    # for string in distinct_strings:
       # print(string)
    # 返回不同字符串的数量
    return len(distinct_strings)

# 读取用户输入的字符串
input_str = input()
# 将输入的字符串按空格分割为两部分，分别为字符串和长度
parts = input_str.split(" ")
s = parts[0]  # 获取输入的字符串
length = int(parts[1])  # 将输入的长度部分转换为整数

# 调用count_distinct_strings方法计算满足条件的不同字符串的数量
count = count_distinct_strings(s, length)
# 输出计算结果
print(count)
