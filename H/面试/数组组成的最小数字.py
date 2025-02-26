import sys

input = sys.stdin.readline().strip()

# 将输入的字符串按逗号分隔成字符串数组
nums = input.split(",")

# 对字符串数组进行排序，按照数字大小排序
nums.sort(key=int)

# 取出前三个数字组成最小数字
min_nums = nums[:min(3, len(nums))]
min_nums.sort(key=lambda x: x+x)

# 将最小数字拼接成字符串
res = "".join(min_nums)

print(res)