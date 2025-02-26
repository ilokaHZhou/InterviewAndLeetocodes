def asteroidCollision(people: list[int]) -> int:
    survivors = []
    for person in people:
        if person == 0:
            return -1
        alive = True
        # 当前人向左逃生，且有人向右逃生时进行决斗
        while alive and person < 0 and survivors and survivors[-1] > 0:
            # 决斗结果：当前人战斗力大于对手
            alive = survivors[-1] < - person
             # 如果战斗力相等或当前人战斗力更大，移除对手
            if survivors[-1] <= -person:
                person = person + survivors[-1] 

                survivors.pop()
            else:
                survivors[-1] = survivors[-1] + person
                print(survivors[-1])
        # 如果当前人仍然存活，将其添加到逃生者列表
        if alive:
            survivors.append(person)
    return len(survivors)

try:
    # 从输入获取人员列表
    people = list(map(int, input().split()))

    # 检查输入是否异常
    if len(people) > 30000:
        raise ValueError("输入异常")

    # 调用函数并输出结果
    result = asteroidCollision(people)
    print(result)
except ValueError as e:
    print(-1)