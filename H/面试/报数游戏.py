def find_last_person(numbers, M):
    while len(numbers) >= M:  # 如果当前人数不小于M，则继续执行
        temp = numbers[M:] + numbers[:M-1]  # 将第M个元素以后的部分和前M-1个元素合并
        numbers = temp  # 更新numbers
    return numbers

 
M = int(input())  # 读入整数M

if M <= 1 or M >= 100:
    print("ERROR!")  # 如果M不在规定范围内，输出错误信息
else:
    numbers = list(range(1, 101))  # 生成1到100的列表
    result = find_last_person(numbers, M)  # 获取最后剩下的人
    result.sort()  # 对结果进行排序

    # 打印结果，用逗号分隔
    print(",".join(map(str, result)))