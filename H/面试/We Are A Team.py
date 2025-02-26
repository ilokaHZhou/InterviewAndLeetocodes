def find(x, parent):
    # 查找节点，用于判断两个人是否在同一个团队
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


# 读取输入，获取人数和消息数量
num_people, num_messages = map(int, input().split())

# 读取消息并存储到二维数组中
messages = [list(map(int, input().split())) for _ in range(num_messages)]

# 检查输入范围，如果超出范围则输出 "Null"
if num_people < 1 or num_people >= 100000 or num_messages < 1 or num_messages >= 100000:
    print("Null")
else:
    # 初始化数组，用于存储每个人的团队信息
    parent = list(range(num_people + 1))

    # 遍历消息，根据指令处理团队关系
    for message in messages:
        person_a, person_b, command = message

        # 检查输入范围，如果超出范围则输出 "da pian zi"
        if person_a < 1 or person_a > num_people or person_b < 1 or person_b > num_people:
            print("da pian zi")
            continue

        # 如果指令为 0，则合并 person_a 和 person_b 所在的团队
        if command == 0:
            root_a = find(person_a, parent)
            root_b = find(person_b, parent)

            if root_a != root_b:
                parent[root_b] = root_a
        # 如果指令为 1，则判断 person_a 和 person_b 是否在同一个团队
        elif command == 1:
            print("We are a team" if find(person_a, parent) == find(person_b, parent) else "We are not a team")
        # 如果指令为其他值，则输出 "da pian zi"
        else:
            print("da pian zi")