# 读取输入的字符串
s = input()

# 创建一个字典用于记录每个字符的出现次数
char_count = {}
# 遍历字符串中的每个字符
for char in s:
    if char in char_count:
        # 若字符已在字典中，出现次数加 1
        char_count[char] += 1
    else:
        # 若字符不在字典中，初始化出现次数为 1
        char_count[char] = 1

# 再次遍历字符串
for char in s:
    if char_count[char] == 1:
        # 若当前字符只出现一次，输出该字符并结束程序
        print(char)
        break
else:
    # 若没有只出现一次的字符，输出 -1
    print(-1)
