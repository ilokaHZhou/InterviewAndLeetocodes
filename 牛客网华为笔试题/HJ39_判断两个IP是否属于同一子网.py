def is_valid_ip(ip):
    parts = ip.split('.')  # 按 '.' 分割 IP 地址
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

def is_valid_mask(mask):
    if not is_valid_ip(mask):  # 如果不是合法 IP
        return False
    binary = ''.join(f"{int(part):08b}" for part in mask.split('.'))  # 转换为二进制
    # 检查掩码是否连续 1 后接连续 0
    if '01' in binary:  # 如果出现 '01'，说明掩码不合法
        return False
    return True  # 如果掩码合法

def is_same_subnet(ip1, ip2, mask):
    def ip_to_int(ip):  # 将 IP 地址转换为整数
        return int(''.join(f"{int(part):08b}" for part in ip.split('.')), 2)
    mask_int = ip_to_int(mask)  # 将掩码转换为整数
    ip1_int = ip_to_int(ip1)  # 将 IP1 转换为整数
    ip2_int = ip_to_int(ip2)  # 将 IP2 转换为整数
    return (ip1_int & mask_int) == (ip2_int & mask_int)  # 判断是否属于同一子网

# 输入处理
mask = input().strip()
ip1 = input().strip()
ip2 = input().strip()

# 判断 IP 和掩码是否合法
if not is_valid_ip(ip1) or not is_valid_ip(ip2) or not is_valid_mask(mask):
    print(1)  # 如果 IP 或掩码不合法，输出 1
else:
    print(0 if is_same_subnet(ip1, ip2, mask) else 2)  # 判断是否属于同一子网