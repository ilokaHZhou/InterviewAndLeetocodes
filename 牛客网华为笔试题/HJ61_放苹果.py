def count_ways(m, n):  # m 个苹果，n 个盘子
    # 基本情况：
    # 1. 如果没有苹果（m == 0），只有一种放法：所有盘子都为空。
    # 2. 如果只有一个盘子（n == 1），只有一种放法：所有苹果放入这个盘子。
    if m == 0 or n == 1:
        return 1

    # 如果盘子数多于苹果数（n > m），
    # 多余的盘子一定为空，因此等价于将 m 个苹果放入 m 个盘子。
    if n > m:
        return count_ways(m, m)

    # 递归情况：
    # 1. 至少一个盘子为空：相当于将 m 个苹果放入 n-1 个盘子。
    # 2. 所有盘子都有苹果：相当于将 m-n 个苹果放入 n 个盘子（每个盘子先放一个苹果）。
    return count_ways(m, n - 1) + count_ways(m - n, n)


# 输入处理
m, n = map(int, input().split())  # 读取苹果数 m 和盘子数 n
print(count_ways(m, n))  # 输出放法的总数
