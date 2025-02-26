import math

def isCoprime(x, y):
    while y > 0:
        mod = x % y
        x = y
        y = mod
    return x == 1

start = int(input()) 
end = int(input()) 

# 将范围内的数的平方存入数组
squares = [i*i for i in range(start, end+1)]

# 将数组转为 set，方便查找
squareSet = set(squares)

# 存储勾股数元组的数组
pythagoreanTriples = []
for i in range(len(squares)):
    for j in range(i+1, len(squares)):
        s = squares[i] + squares[j]
        if s in squareSet:
            pythagoreanTriples.append([int(math.sqrt(squares[i])), int(math.sqrt(squares[j])), int(math.sqrt(s))])

# 存储符合条件的勾股数元组的数组
coprimeTriples = []
for triple in pythagoreanTriples:
    if isCoprime(triple[0], triple[1]) or isCoprime(triple[0], triple[2]) or isCoprime(triple[1], triple[2]):
        coprimeTriples.append(triple)

# 按照题目要求排序输出
if not coprimeTriples:
    print("NA")
else:
    coprimeTriples.sort(key=lambda x: (x[0], x[1], x[2]))
    for triple in coprimeTriples:
        print(triple[0], triple[1], triple[2])