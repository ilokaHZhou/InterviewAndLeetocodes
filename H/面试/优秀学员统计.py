import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math
import sys

# 比较函数，按照打卡次数、首次打卡时间、员工ID的顺序进行排序
def compare(a, b):
    if (a[1] == b[1]): # 如果打卡次数相同
        if (a[2] == b[2]): # 如果首次打卡时间相同
            return a[0] - b[0] # 按照员工ID升序排列
        else:
            return a[2] - b[2] # 按照首次打卡时间升序排列
    else:
        return b[1] - a[1] # 按照打卡次数降序排列

# 新员工数量
num_new_employees = int(input())
# 每天打卡的员工数量
employee_count_per_day = [int(x) for x in input().split(" ")]
# 打卡记录
employee_records = []
for i in range(30):
    employee_records.append([int(x) for x in input().split(" ")])

# key为员工ID， value为其打卡的记录信息：[打卡次数，首次打卡index]
employee_info = {}
for i in range(30):
    for j in employee_records[i]:
        if(j in employee_info): # 如果员工已经在字典中
            employee_info[j][0] += 1 # 打卡次数加1
        else:
            employee_info[j] = [1, i] # 否则，将员工添加到字典中，并记录打卡次数和首次打卡时间

# 将map信息转到list中，以便后续排序
employee_list = []
for key in employee_info:
    employee_list.append([key, employee_info[key][0], employee_info[key][1]]);

# 按照打卡次数、首次打卡时间、员工ID的顺序进行排序
employee_list = sorted(employee_list, key=functools.cmp_to_key(compare));

res = []
for i in range(5):
    res.append(str(employee_list[i][0]))

# 输出
print(" ".join(res))