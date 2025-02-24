def ip_to_int(ip):
    parts = list(map(int, ip.split(".")))
    result = 0
    for part in parts:
        # 将二进制数向左移动指定的位数，右侧补0，并令其与part二进制数的每一位进行或运算，只要有一个是 1，结果就是 1，其实就是二进制左移然后对应的十进制数累加
        result = (result << 8) | part
    return result


def int_to_ip(num):
    ip_parts = []
    for _ in range(4):
        # 对两个二进制数的每一位进行与运算，只有两个都是 1，结果才是 1。
        # 0xFF：十六进制数 0xFF 表示二进制的 11111111（8 个 1）。
        # num & 0xFF 会保留 num 的最低 8 位，其余位变为 0。
        ip_parts.append(str(num & 0xFF))
        num >>= 8
    return ".".join(reversed(ip_parts))


# 多组输入处理
while True:
    try:
        line = input().strip()
        if "." in line:  # 输入是IP地址
            print(ip_to_int(line))
        else:  # 输入是整数
            print(int_to_ip(int(line)))
    except EOFError:
        break
