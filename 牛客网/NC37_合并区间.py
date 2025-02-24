# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param intervals Interval类一维数组
# @return Interval类一维数组
#
class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        # 先排个序这样所有列表的左端点都从小到大排列了
        intervals.sort(key=lambda x: x.start)  # 按照每个列表的第一个元素进行升序排列
        merged = []
        for interval in intervals:
            # 如果merged列表为空或者两个列表没有交集（前一个列表的最大值小于后一个列表的最小值）
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            # 如果需要合并，不用管左端点因为下一个列表左端点一定比前一个多左端点大
            # 所以只需看merged最后一个元素的右端点和新列表的右端点哪个大即可
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged
