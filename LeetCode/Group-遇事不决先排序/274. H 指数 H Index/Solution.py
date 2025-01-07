'''
从大到小排列，h一定能插在其中两数之间，使得身前皆为引用多于h次的，h后皆为引用少于h次的
i + 1为引用多于h的文献的次数，要加1是因为index从0开始，
如果满足h身前的文献的引用次数至少是i + 1，则i+1便是h指数
但因为 h 有多种可能的值，h 指数 是其中最大的那个
因此转化为求i + 1的最大值
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        orderedList = sorted(citations, reverse=True)
        print(orderedList)
        h = 0
        for i in range(len(orderedList)):
            if orderedList[i] >= i + 1:
                h = i + 1
        return h