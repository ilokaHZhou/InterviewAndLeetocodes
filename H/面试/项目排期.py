# Python版本代码
from itertools import combinations

def minimumTimeRequired(tasks, k):
    # 将任务按工作量降序排序
    tasks.sort(reverse=True)
    
    # 使用二分查找确定完成所有任务的最短时间
    l, r = tasks[0], sum(tasks)
    while l < r:
        mid = (l + r) // 2
        # 检查当前时间限制是否足够完成所有任务
        if canFinish(tasks, k, mid):
            r = mid
        else:
            l = mid + 1
    
    # 返回最短完成时间
    return l

def canFinish(tasks, k, limit):
    # 创建一个数组来记录每个员工的工作量
    workers = [0] * k
    # 使用回溯法检查是否可以完成
    return backtrack(tasks, workers, 0, limit)

def backtrack(tasks, workers, index, limit):
    # 如果所有任务都已分配，则返回True
    if index >= len(tasks):
        return True
    
    # 获取当前任务的工作量
    current = tasks[index]
    # 尝试将当前任务分配给每个员工
    for i in range(len(workers)):
        # 如果当前员工可以在时间限制内完成这项任务
        if workers[i] + current <= limit:
            # 分配任务给当前员工
            workers[i] += current
            # 继续尝试分配下一个任务
            if backtrack(tasks, workers, index + 1, limit):
                return True
            # 回溯，取消当前的任务分配
            workers[i] -= current
        
        # 如果当前员工没有任务或者加上当前任务刚好达到时间限制，则不需要尝试其他员工
        if workers[i] == 0 or workers[i] + current == limit:
            break
    
    # 如果无法分配当前任务，则返回False
    return False

if __name__ == "__main__":
    # 使用input读取输入
    tasks = list(map(int, input().split()))
    N = int(input())
    
    # 输出最快完成所有工作的天数
    print(minimumTimeRequired(tasks, N))