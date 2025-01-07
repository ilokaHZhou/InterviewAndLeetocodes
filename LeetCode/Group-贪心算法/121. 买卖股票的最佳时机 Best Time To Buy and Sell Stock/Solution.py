'''
如果每次遍历都要去当前元素后的子序列找最大值会超时，最好是每次遍历，更新i天前股票的最小值
然后再比较利润，这样一次遍历O(n)即可完成

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        for item in prices:
            maxProfit = max(item - minPrice, maxProfit) # max写在min前面，否则minPrice更新会影响max判断
            minPrice = min(minPrice, item)
        return maxProfit