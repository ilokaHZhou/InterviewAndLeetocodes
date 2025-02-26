from collections import defaultdict

# 输入exclude和s
exclude = input()
s = input()
# 获取要排除的字符
excludeChar = exclude[0]

# 存储每个字符出现的下标
charIndexMap = defaultdict(list)

# 定义左右指针
left = 0
right = 0

# 定义最长子串长度
maxLength = 0

# 遍历字符串
while right < len(s):
    currentChar = s[right]

    # 如果当前字符是要排除的字符
    if excludeChar == currentChar:
        # 如果左右指针不在同一位置，说明存在符合条件的子串
        if right > left:
            maxLength = max(maxLength, right - left)
        # 将左右指针都移动到下一个位置
        right += 1
        left = right
    else:
        # 如果当前字符不是要排除的字符
        # 先将当前字符在map中初始化
        charIndexMap[currentChar]
        charIndexes = charIndexMap[currentChar]
        # 如果当前字符的出现次数已经超过2次
        if len(charIndexes) == 2:
            # 更新最长子串长度
            maxLength = max(maxLength, right - left)
            # 将左指针移动到当前字符上一次出现的位置的下一个位置
            left = charIndexes[0] + 1
            # 删除当前字符在map中的第一个下标
            charIndexes.pop(0)
        # 将当前字符的下标加入map中
        charIndexes.append(right)
        # 右指针向后移动
        right += 1

# 检查最后一个子串是否符合条件
maxLength = max(maxLength, right - left)

# 输出最长子串长度
print(maxLength)