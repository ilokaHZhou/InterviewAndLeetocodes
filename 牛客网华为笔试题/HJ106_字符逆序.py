words = input().strip().split(' ')
# reversed返回的是一个反向迭代器，所以需要创建新序列，占用内存较少
words = list(reversed(words))
# [::-1]切片直接返回新序列，但占用内存较大，适用于小序列
words = [word[::-1] for word in words]
print(' '.join(words))
