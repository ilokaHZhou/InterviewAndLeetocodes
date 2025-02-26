from collections import deque

number = int(input()) # 数据的范围

queue = deque() # 模拟双端队列
in_order = True # 是否按顺序删除
result = 0 # 最小的调整顺序次数

for i in range(2 * number):
    input_str = input()
    operation = input_str.split(" ")
    if operation[0] == "head": # 从头部添加元素
        if len(queue) != 0 and in_order: # 不按顺序删除
            in_order = False
        queue.appendleft(int(operation[2]))
    elif operation[0] == "tail": # 从尾部添加元素
        queue.append(int(operation[2]))
    else: # 删除元素
        if len(queue) == 0:
            continue
        if not in_order: # 不按顺序删除
            result += 1
            in_order = True
        queue.pop()

print(result) # 输出最小的调整顺序次数