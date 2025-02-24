def is_leap_year(year):  # 判断是否为闰年
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def date_to_days(year, month, day):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 每月的天数
    if is_leap_year(year):  # 如果是闰年，2月有29天
        month_days[2] = 29
    total_days = sum(month_days[:month]) + day  # 计算总天数
    return total_days


# 输入处理
year, month, day = map(int, input().split())
print(date_to_days(year, month, day))
