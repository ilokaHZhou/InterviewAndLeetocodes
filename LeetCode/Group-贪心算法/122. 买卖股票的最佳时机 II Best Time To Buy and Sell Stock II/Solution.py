'''
使用贪心算法
假如第 0 天买入，第 3 天卖出，那么利润为：prices[3] - prices[0]。

相当于(prices[3] - prices[2]) + (prices[2] - prices[1]) + (prices[1] - prices[0])。

此时就是把利润分解为每天为单位的维度，而不是从 0 天到第 3 天整体去考虑！
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int: # 检查每过一天利润的差额，只取所有的正利润之和即可达到利润最大化
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0)
        return result