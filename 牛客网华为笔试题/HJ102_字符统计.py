s = input().strip()
chars = {}
for c in s:
    if c in chars:
        chars[c] += 1
    else:
        chars[c] = 1

# 对字典进行排序，先按出现次数降序排序，如果次数相同则按字符的 ASCII 码升序排序
# item[1]是value，item[0]是key，-item[1]前面加负号 - 是为了实现按出现次数降序排序。因为在 Python 的排序规则里，默认是升序，加负号后就相当于把大的数值变成小的负数，从而实现降序效果。
# 这里返回的是一个元组列表
sorted_chars = sorted(chars.items(), key=lambda item: (-item[1], item[0]))

result = ''.join([item for item, _ in sorted_chars])
print(result)