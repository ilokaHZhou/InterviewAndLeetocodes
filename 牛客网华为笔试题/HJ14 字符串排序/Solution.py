# 读取字符串的个数
n = int(input())

# 读取 n 个字符串
words = [input().strip() for _ in range(n)]

# 对字符串进行升序排序
sorted_words = sorted(words)

# 输出排序后的结果
for word in sorted_words:
    print(word)