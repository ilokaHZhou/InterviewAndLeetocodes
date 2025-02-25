def encrypt_string(key, s):
    # 生成加密字母表
    key = key.upper()  # 将密钥转换为大写
    used = set()  # 记录已使用的字母
    encrypted_alphabet = []  # 加密字母表
    for char in key:  # 遍历密钥
        if char not in used:  # 如果字母未使用过
            encrypted_alphabet.append(char)  # 添加到加密字母表
            used.add(char)  # 标记为已使用
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  # 遍历剩余字母
        if char not in used:  # 如果字母未使用过
            encrypted_alphabet.append(char)  # 添加到加密字母表
    # 加密字符串
    result = []
    for char in s:  # 遍历字符串
        if char.isupper():  # 如果是大写字母
            index = ord(char) - ord("A")  # 计算字母索引
            result.append(encrypted_alphabet[index])  # 添加加密字母
        elif char.islower():  # 如果是小写字母
            index = ord(char) - ord("a")  # 计算字母索引
            result.append(encrypted_alphabet[index].lower())  # 添加加密字母（小写）
        else:  # 如果是其他字符
            result.append(char)  # 直接添加
    return "".join(result)  # 返回加密后的字符串


# 输入处理
key = input().strip()
s = input().strip()
print(encrypt_string(key, s))
