import re

# 读取输入字符串
s = input()

# 定义匹配非法字符的正则表达式（非数字和小写字母的字符）
pat = "[^0-9a-z]"

# 用于存储数字部分的字符串
num = ""

# 用于存储最终解压缩的结果
res = ""

# 编译正则表达式并查找非法字符
pattern = re.compile(pat)
matcher = pattern.search(s)

# 如果找到非法字符，则直接输出 "!error"
if matcher:
    res = "!error"
else:
    # 遍历输入字符串的每一个字符
    for i in range(len(s)):
        c = s[i]
        
        # 如果当前字符是数字，则将其追加到 num 中
        if c.isdigit():
            num += c
        # 如果 num 不为空，表示之前有数字，需要进行解压操作
        elif num != "":
            # 判断数字是否小于等于2，如果是则输入不合法
            if int(num) <= 2:
                res = "!error"
                break
            else:
                # 将对应数量的字母添加到结果中
                for j in range(int(num)):
                    res += c
                # 重置 num 为空
                num = ""
        # 如果当前字符是字母，且前面没有数字，则直接添加到结果中
        else:
            res += c

# 输出最终结果
print(res)