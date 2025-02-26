import sys

input = sys.stdin.readline().strip() # 输入任务序列，以逗号分隔
tasks = [] # 定义任务列表
num = ""
for c in input: # 遍历输入字符串
    if c == ',': # 如果遇到逗号
        tasks.append(int(num)) # 将当前数字字符串转换为整数并加入任务列表
        num = "" # 清空数字字符串
    else:
        num += c # 否则将当前字符加入数字字符串
if num != "": # 如果数字字符串不为空
    tasks.append(int(num)) # 将其转换为整数并加入任务列表
waitTime = int(sys.stdin.readline()) # 输入等待时间
count = {} # 定义字典，用于统计每个任务出现的次数
for t in tasks:
    if t in count:
        count[t] += 1 # 统计任务出现次数
    else:
        count[t] = 1
taskList = [] # 定义任务列表，每个任务用一个列表表示，第一个元素为剩余次数，第二个元素为等待时间
for t, c in count.items(): # 遍历字典
    taskList.append([c, 0]) # 将每个任务的出现次数加入任务列表
taskList.sort(key=lambda x: x[0], reverse=True) # 按照任务出现次数从大到小排序
total = len(tasks) # 总任务数
time = 0 # 当前时间
while total > 0: # 当还有任务未完成时
    time += 1 # 时间加一
    flag = True # 标记是否已经有任务开始执行
    for task in taskList: # 遍历任务列表
        if flag and task[0] > 0 and task[1] == 0: # 如果当前任务未执行且等待时间为零且还未有任务开始执行
            flag = False # 将标记设为false，表示已经有任务开始执行
            task[0] -= 1 # 当前任务剩余次数减一
            total -= 1 # 总任务数减一
            task[1] = waitTime # 将当前任务的等待时间设为输入的等待时间
        else:
            if task[1] > 0: # 如果当前任务正在等待
                task[1] -= 1 # 等待时间减一
print(time) # 输出完成所有任务所需的最短时间