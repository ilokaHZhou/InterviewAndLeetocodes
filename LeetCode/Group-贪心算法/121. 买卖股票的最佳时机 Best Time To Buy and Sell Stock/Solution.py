'''
遍历每天股价，看是否当前股价与历史最低点的价差最大，然后不断更新历史最低点和最大收益值

如果每次遍历都要去当前元素后的子序列找最大值会超时，最好是每次遍历，更新i天前股票的最小值
然后再比较利润，这样一次遍历O(n)即可完成

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        for item in prices:
            # max写在min前面，否则minPrice更新会影响max判断
            maxProfit = max(item - minPrice, maxProfit)
            # 先更新当前元素计算的maxProfit再更新minPrice
            minPrice = min(minPrice, item)
        return maxProfit