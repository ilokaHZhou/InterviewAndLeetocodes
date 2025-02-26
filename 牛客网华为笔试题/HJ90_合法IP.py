def is_valid_ip(ip):
    parts = ip.split(".")  # 按 '.' 分割 IP 地址
    if len(parts) != 4:  # 如果不是 4 部分
        return False
    for part in parts:  # 遍历每一部分
        if not part.isdigit():  # 如果不是数字
            return False
        num = int(part)
        if num < 0 or num > 255:  # 如果不在 0-255 范围内
            return False
        if part != str(num):  # 如果有前导零
            return False
    return True  # 如果所有部分都合法


# 输入处理
ip = input().strip()
print("YES" if is_valid_ip(ip) else "NO")
