# 第三个月 n = 1 + 1 = 2
# 第四个月 n = 2 + 1 = 3
# 第五个月 n = 3 + 1 + 1 = 5 = (n - 2) + (n - 1)
# 第六个月 n = 5 + 1 + 2 = 8 = (n - 2) + (n - 1)
def count_rabbits(month):
    if month == 1 or month == 2:
        return 1
    prev, curr = 1, 1
    for _ in range(3, month + 1):
        prev, curr = curr, prev + curr
    return curr


month = int(input())
print(count_rabbits(month))
