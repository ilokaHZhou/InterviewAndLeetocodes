# 判断一个数是否为素数
def is_prime(num):
    # 素数是大于1且只能被1和自身整除的数
    if num < 2:
        return False
    # 从2开始到该数的平方根进行遍历判断
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 匈牙利算法，用于寻找增广路径
def find_path(u, match, vis, graph):
    # 遍历与u相连的所有顶点
    for v in graph[u]:
        if not vis[v]:
            vis[v] = True
            # 如果v未匹配或者可以找到增广路径
            if match[v] == -1 or find_path(match[v], match, vis, graph):
                match[v] = u
                return True
    return False


while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        # 分离奇数和偶数
        odd_nums = []
        even_nums = []
        for num in nums:
            if num % 2 == 0:
                even_nums.append(num)
            else:
                odd_nums.append(num)

        # 构建二分图
        graph = [[] for _ in range(len(odd_nums))]
        for i, odd in enumerate(odd_nums):
            for j, even in enumerate(even_nums):
                # 如果两数之和为素数，则在图中添加边
                if is_prime(odd + even):
                    graph[i].append(j)

        # 初始化匹配数组
        match = [-1] * len(even_nums)
        result = 0
        # 对每个奇数顶点进行匹配尝试
        for i in range(len(odd_nums)):
            vis = [False] * len(even_nums)
            if find_path(i, match, vis, graph):
                result += 1

        print(result)
    except:
        break
