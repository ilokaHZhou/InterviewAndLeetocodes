# 定义一个函数，用于将给定的16进制字符串转换为整数
# length_str 是两个16进制字符拼接后的字符串（表示长度）
def get_length(length_str):
    return int(length_str, 16)  # 将16进制字符串转换为10进制整数

# 主函数
def main():
    # 从用户输入中获取目标Tag，并去除首尾空白字符
    tag = input().strip()

    # 从用户输入中获取码流数据，并去除首尾空白字符
    line = input().strip()

    # 将码流数据按空格分割，存入hex_array数组中，每个元素是一个16进制字符串
    hex_array = line.split(" ")

    index = 0  # 初始化索引，用于遍历 hex_array

    # 使用while循环遍历整个hex_array
    while index < len(hex_array):
        # 解析当前信元的 Length 字段
        # Length 字段由两个字节组成，先拼接hex_array[index+2]（高位）和hex_array[index+1]（低位）
        # 再调用get_length函数将其转换为十进制整数
        length = get_length(hex_array[index + 2] + hex_array[index + 1])

        # 如果当前信元的Tag与输入的Tag匹配
        if hex_array[index] == tag:
            sb = []  # 定义一个空列表，用于存储匹配Tag后的Value部分

            # 从index+3位置开始（即第一个Value字节），提取length个字节的Value
            for i in range(index + 3, index + 3 + length):
                sb.append(hex_array[i])  # 将每个字节加入sb列表

            # 输出提取的Value部分，使用空格连接，并将输出转换为大写，去掉首尾多余空格
            print(" ".join(sb).upper().strip())
            break  # 找到匹配的Tag后，结束循环
        else:
            # 如果当前Tag不匹配，则跳过当前信元
            # 跳过的字节数为：1 个 Tag + 2 个 Length + length 个 Value
            index += (2 + length + 1)

# 检查是否在直接运行脚本
if __name__ == "__main__":
    main()  # 调用主函数