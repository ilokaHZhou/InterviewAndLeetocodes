# 定义一个函数，用于找出满足条件的最长子字符串的长度
def find_longest_substring_length(s):
    # 获取输入字符串的长度
    n = len(s)
    # 初始化最长子字符串长度为 0
    max_length = 0

    # 外层循环，从字符串的每一个字符开始检查
    for i in range(n):
        # 初始化 'l'、'o' 和 'x' 的计数器
        count_l = 0
        count_o = 0
        count_x = 0

        # 内层循环，从当前字符开始，遍历整个字符串
        for j in range(n):
            # 计算当前字符的索引，处理环形字符串的情况
            index = (i + j) % n
            # 获取当前字符
            ch = s[index]

            # 根据当前字符增加相应字符的计数
            if ch == 'l':
                count_l += 1
            elif ch == 'o':
                count_o += 1
            elif ch == 'x':
                count_x += 1

            # 如果 'l'、'o' 和 'x' 出现的次数都是偶数
            if count_l % 2 == 0 and count_o % 2 == 0 and count_x % 2 == 0:
                # 更新最长子字符串的长度
                max_length = max(max_length, j + 1)

    # 返回最长子字符串的长度
    return max_length

# 主函数
if __name__ == '__main__':
    # 从标准输入读取字符串
    s = input()
    # 调用 find_longest_substring_length 函数计算并返回结果
    result = find_longest_substring_length(s)
    # 打印结果
    print(result)