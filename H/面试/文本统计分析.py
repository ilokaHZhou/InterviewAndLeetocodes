import sys

# 统计文本中的文本数量
def count_texts(input):
    # 初始化计数器
    count = 0
    # 标记是否在字符串内部
    in_string = False
    # 标记是否在注释内部
    in_comment = False
    # 记录字符串分隔符
    string_delimiter = ''
    # 标记当前是否为空文本（即没有遇到非空白字符）
    isEmpty = True

    # 遍历输入文本的每个字符
    for i, c in enumerate(input):
        # 下一个字符（如果存在）
        next_char = input[i + 1] if i + 1 < len(input) else '\0'

        # 如果在注释中
        if in_comment:
            # 如果遇到换行符，则注释结束
            if c == '\n':
                in_comment = False
            continue

        # 如果遇到连续的两个减号，并且不在字符串内，则进入注释状态
        if c == '-' and next_char == '-' and not in_string:
            in_comment = True
            i += 1  # 跳过下一个减号
            continue

        # 如果遇到单引号或双引号，并且不在字符串内，则进入字符串状态
        if (c == '\'' or c == '\"') and not in_string:
            in_string = True
            string_delimiter = c
            isEmpty = False
            continue

        # 如果在字符串内，并且遇到了相同的分隔符，则检查是否为转义
        if c == string_delimiter and in_string:
            if next_char == string_delimiter:
                i += 1  # 跳过转义的引号
            else:
                in_string = False  # 字符串结束
            continue

        # 如果遇到分号，并且不在字符串内，则增加计数器
        if c == ';' and not in_string:
            if not isEmpty:
                count += 1
                isEmpty = True
            continue

        # 如果遇到非空白字符，并且不在字符串内，则标记为非空文本
        if not c.isspace() and not in_string:
            isEmpty = False

    # 如果最后一个文本没有闭合的分号，则增加计数器
    if not isEmpty:
        count += 1  # 最后一个文本没有闭合分号

    return count

# 主函数
if __name__ == "__main__":
    # 使用字符串来构建整个输入文本
    input = sys.stdin.read()
    # 输出文本统计结果
    print(count_texts(input))