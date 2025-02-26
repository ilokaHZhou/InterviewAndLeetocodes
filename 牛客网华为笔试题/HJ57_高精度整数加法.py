# 读取两个大整数输入
num1 = input()
num2 = input()

# 初始化进位为 0
carry = 0
# 用于存储结果的列表
result = []

# 从两个数的末尾开始逐位相加
i, j = len(num1) - 1, len(num2) - 1
while i >= 0 or j >= 0 or carry:
    # 获取当前位的数字，如果已经遍历完则取 0
    digit1 = int(num1[i]) if i >= 0 else 0
    digit2 = int(num2[j]) if j >= 0 else 0
    # 计算当前位的和以及进位
    total = digit1 + digit2 + carry
    carry = total // 10
    digit = total % 10
    # 将当前位的结果添加到结果列表
    result.append(str(digit))
    # 移动到前一位
    i -= 1
    j -= 1

# 将结果列表反转并拼接成字符串
final_result = "".join(result[::-1])
# 输出最终结果
print(final_result)
