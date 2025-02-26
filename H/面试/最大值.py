# 导入需要的模块
import functools

# 读取输入并分割
input_str = input().split()

# 将字符串数组转换为整数数组
nums = [int(i) for i in input_str]

# 将整数数组转换为字符串数组
str_nums = [str(num) for num in nums]

# 定义自定义排序规则，比较两个字符串拼接后的大小
def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

# 对字符串数组进行排序
str_nums.sort(key=functools.cmp_to_key(compare))

# 拼接排序后的字符串
result = ''.join(str_nums)

# 去除前导零，如果全是零，则只返回一个零
result = result.lstrip('0') or '0'

# 输出最终结果
print(result)