def sort_string(s):
    # 提取字母字符并排序
    letters = sorted([char for char in s if char.isalpha()], key=lambda x: x.lower())
    # 构建结果字符串
    result = []
    idx = 0
    for char in s:
        if char.isalpha():
            result.append(letters[idx])
            idx += 1
        else:
            result.append(char)
    return ''.join(result)

# 读取输入
s = input().strip()
# 输出结果
print(sort_string(s))