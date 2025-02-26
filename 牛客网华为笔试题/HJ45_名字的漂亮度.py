# 读取输入的名字数量
n = int(input())

# 循环处理每个名字
for _ in range(n):
    # 读取名字
    name = input().lower()
    # 用于存储每个字母的出现次数
    letter_count = {}
    # 遍历名字中的每个字母
    for letter in name:
        if letter.isalpha():
            # 如果字母已经在字典中，次数加1
            if letter in letter_count:
                letter_count[letter] += 1
            # 否则，将该字母的出现次数初始化为1
            else:
                letter_count[letter] = 1
    # 提取所有字母的出现次数，并按降序排序
    counts = sorted(letter_count.values(), reverse=True)
    # 初始化漂亮度为0
    beauty = 0
    # 从26开始，依次为出现次数多的字母分配较高的漂亮度值
    value = 26
    # 遍历排序后的出现次数列表
    for count in counts:
        # 计算当前字母的漂亮度并累加到总漂亮度中
        beauty += count * value
        # 漂亮度值减1
        value -= 1
    # 输出该名字的漂亮度
    print(beauty)