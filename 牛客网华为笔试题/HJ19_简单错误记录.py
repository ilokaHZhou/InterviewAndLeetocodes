def error_records(records):
    error_count = {}  # 存储错误记录及其出现次数
    order = []  # 存储错误记录的顺序
    for record in records:  # 遍历错误记录
        file_name, line_num = record.split()  # 分割文件名和行号
        file_name = file_name.split("\\")[-1][-16:]  # 提取文件名最后 16 个字符
        key = (file_name, line_num)  # 构建错误记录的键
        if key not in error_count:  # 如果键不存在
            error_count[key] = 1  # 初始化计数
            order.append(key)  # 记录顺序
        else:  # 如果键已存在
            error_count[key] += 1  # 计数加 1
    # 输出最后 8 条记录
    for key in order[-8:]:
        file_name, line_num = key
        print(f"{file_name} {line_num} {error_count[key]}")


# 输入处理
records = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        records.append(line)
    except EOFError:
        break

# 调用函数
error_records(records)
