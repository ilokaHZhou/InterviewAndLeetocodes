s = input()

# 对字符串进行排序
sortedArr = sorted(s)

# 如果排序后的字符串与原字符串相同，则说明已经是最小字符串，直接输出
if ''.join(sortedArr) == s:
    print(s)
    exit()

# 遍历原字符串
sb = list(s)
for i in range(len(s)):
    # 如果当前字符与排序后的字符不相同，则进行交换
    if s[i] != sortedArr[i]:
        tmp = sb[i]
        swapIndex = -1
        # 找到排序后的字符在原字符串中的位置
        for j in range(i + 1, len(s)):
            if sb[j] == sortedArr[i]:
                swapIndex = j
        # 将原字符与排序后的字符交换
        sb[i] = sortedArr[i]
        sb[swapIndex] = tmp
        break

# 输出最小字符串
print(''.join(sb))