import sys

str1 = input() #读入字符串

count = [0] * 256 #用一个数组记录每个字符出现的次数
for ch in str1:
    count[ord(ch)] += 1

max_count = max(count) #获取出现次数最多的字符的出现次数
result = ""
for i in range(max_count, 0, -1): #从出现次数最多的开始遍历
    for j in range(ord('a'), ord('z')+1): #先输出小写字母
        if count[j] == i:
            result += chr(j)
            result += ":"
            result += str(i)
            result += ";"
    for j in range(ord('A'), ord('Z')+1): #再输出大写字母
        if count[j] == i:
            result += chr(j)
            result += ":"
            result += str(i)
            result += ";"

print(result)