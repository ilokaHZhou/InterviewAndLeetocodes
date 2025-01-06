class Solution:
    def maxProfit(self, prices: List[int]) -> int: # 检查每过一天利润的差额，只取所有的正利润之和即可达到利润最大化
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0)
        return result