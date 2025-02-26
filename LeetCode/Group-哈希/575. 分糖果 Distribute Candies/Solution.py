class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # 计算糖果的总种类数
        unique_candies = len(set(candyType))
        # 计算女孩可以分到的最大糖果数量
        max_candies = len(candyType) // 2
        # 返回女孩可以获得的最大糖果种类数
        return min(unique_candies, max_candies)