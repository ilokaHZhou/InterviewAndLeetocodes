# 读取胡杨树的总数N
total = int(input())

# 读取未成活胡杨树的数量M
dead_count = int(input())

# 读取未成活胡杨树的编号列表
dead_list = list(map(int, input().split()))

# 读取可以补种的胡杨树数量K
supplement_count = int(input())

# 初始化数组，所有树最初都是成活的，0表示成活，1表示未成活
nums = [0] * total

# 根据输入，将未成活的树的位置标记为1
for num in dead_list:
    nums[num - 1] = 1  # 树的编号从1开始，因此需要减1

# 初始化滑动窗口的左右边界
left = 0
max_len = 0  # 用于存储最大连续成活区域的长度
sum_left = 0  # 滑动窗口左边界的未成活树数量
sum_right = 0  # 滑动窗口右边界的未成活树数量

# 遍历所有的树，right代表滑动窗口的右边界
for right in range(total):
    sum_right += nums[right]  # 更新右边界的未成活树数量
    
    # 如果窗口内的未成活树数量大于可以补种的数量
    while sum_right - sum_left > supplement_count:
        sum_left += nums[left]  # 缩小窗口，左边界右移
        left += 1
    
    # 更新最大成活区域的长度
    max_len = max(max_len, right - left + 1)

# 输出最大连续成活区域的长度
print(max_len)