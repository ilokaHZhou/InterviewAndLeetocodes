# 先找最大值再比对即可
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = [candy + extraCandies >= maxCandies for candy in candies]
        return result
