def reverse_words(s):
    # 替换非字母字符为空格
    for char in s:
        if not char.isalpha():
            s = s.replace(char, ' ')
    # 分割单词并反转
    words = s.split()
    words.reverse()
    return ' '.join(words)

# 读取输入
s = input().strip()
# 输出结果
print(reverse_words(s))

