import sys

res = sys.maxsize
totalSum = 0
targetSum = 0

# 深度优先搜索函数
def dfs(nums, idx, count, currentSum):
    global res, totalSum, targetSum
    # 剪枝条件：如果当前总和超过目标，则停止.考友反馈，去掉可得100%
    # if currentSum > targetSum:
    #    return

    # 当我们为一个队伍选择了5名玩家时
    if count == 5:
        # 计算另一个队伍的总和
        otherTeamSum = totalSum - currentSum
        # 用较小的差值更新结果
        res = min(res, abs(currentSum - otherTeamSum))
        return

    # 如果我们已经考虑了所有玩家，停止递归
    if idx == 10:
        return

    # 为第一个队伍选择当前玩家
    dfs(nums, idx + 1, count + 1, currentSum + nums[idx])
    
    # 不为第一个队伍选择当前玩家
    dfs(nums, idx + 1, count, currentSum)

nums = list(map(int, input().split()))
for num in nums:
    totalSum += num
targetSum = totalSum // 2
dfs(nums, 0, 0, 0)
print(res)