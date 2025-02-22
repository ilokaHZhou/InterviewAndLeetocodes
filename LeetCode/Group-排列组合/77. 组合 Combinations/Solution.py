"""
既然是树形问题上的 深度优先遍历，因此首先画出树形结构。例如输入：n = 4, k = 2，我们可以发现如下递归结构：

如果组合里有1，那么需要在[2, 3, 4]里再找1个数；
如果组合里有2，那么需要在[3, 4]里再找1数。注意：这里不能再考虑1，因为包含1的组合，在第 1 种情况中已经包含。

回溯问题 + 剪枝
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, track = [], []
        self.backtrack(n, k, 1, track, result)
        return result

    def backtrack(self, n, k, start, track, result):
        if k == 0:
            result.append(track[:])
            return
        for i in range(start, n-k+2):
            track.append(i)
            self.backtrack(n, k-1, i+1, track, result)
            track.pop()