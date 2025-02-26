def can_receive_award(records):
    absent_count = 0  # 用于记录缺勤的次数
    for i in range(len(records)):  # 遍历考勤记录
        if records[i] == "absent":  # 如果记录为缺勤
            absent_count += 1  # 缺勤次数加1
            if absent_count > 1:  # 如果缺勤超过1次
                return False  # 返回False，表示不能获得考勤奖
        if records[i] in ["late", "leaveearly"]:  # 如果记录为迟到或早退
            # 如果前一天也是迟到或早退，则不能获得考勤奖
            if i > 0 and records[i - 1] in ["late", "leaveearly"]:
                return False
        if i >= 6:  # 如果记录长度大于等于7，检查任意连续7天的考勤记录
            # 计算连续7天内非出勤的天数
            count_in_7_days = sum(1 for j in range(i - 6, i + 1) if records[j] != "present")
            if count_in_7_days > 3:  # 如果连续7天内非出勤天数超过3天
                return False  # 返回False，表示不能获得考勤奖
    return True  # 所有条件都满足，返回True，表示可以获得考勤奖

# 读取测试用例的数量
test_cases = int(input().strip())
results = []  # 用于存储每个测试用例的结果
for _ in range(test_cases):  # 遍历每个测试用例
    # 读取并分割每个测试用例的考勤记录
    attendance_records = input().strip().split()
    # 判断是否能获得考勤奖，并将结果添加到results列表中
    results.append("true" if can_receive_award(attendance_records) else "false")
# 输出所有测试用例的结果，结果之间用空格分隔
print(" ".join(results))