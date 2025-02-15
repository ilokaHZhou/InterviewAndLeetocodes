class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先排个序这样所有列表的左端点都从小到大排列了
        intervals.sort(key=lambda x: x[0]) # 按照每个列表的第一个元素进行升序排列
        merged = []
        for interval in intervals:
            # 如果merged列表为空或者两个列表没有交集（前一个列表的最大值小于后一个列表的最小值）
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # 如果需要合并，不用管左端点因为下一个列表左端点一定比前一个多左端点大
            # 所以只需看merged最后一个元素的右端点和新列表的右端点哪个大即可
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged