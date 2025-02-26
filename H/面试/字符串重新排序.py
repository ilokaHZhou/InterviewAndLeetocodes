import collections
import functools

input = input()
words = input.split(" ")

# 对每个单词内部进行字典序排序
words = ["".join(sorted(word)) for word in words]

# 统计每个单词出现的次数
count = collections.Counter(words)

# 按照要求排序
words = sorted(words, key=functools.cmp_to_key(lambda a, b: count[b] - count[a] if count[a] != count[b] else len(a) - len(b) if len(a) != len(b) else -1 if a < b else 1))

# 输出处理后的字符串
output = " ".join(words)
print(output)