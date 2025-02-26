nums = list(map(int, input().split(',')))
target = int(input())

n = len(nums)
left, right, sum_, max_len = 0, 0, 0, -1

while right < n:
    # 不断扩大窗口，增加右边界
    sum_ += nums[right]
    right += 1

    # 如果当前窗口内的和大于目标值，收缩左边界
    while sum_ > target and left < right:
        sum_ -= nums[left]
        left += 1

    # 检查是否等于目标值，并更新最大长度
    if sum_ == target:
        max_len = max(max_len, right - left)

# 输出结果
print(max_len)