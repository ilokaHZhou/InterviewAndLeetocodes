class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, combination):
            result.append(combination[:])
            for i in range(index, len(nums)):
                # 选择当前元素
                combination.append(nums[i])
                # 递归处理下一个元素
                backtrack(i + 1, combination)
                # 撤销选择（回溯）
                combination.pop()
        backtrack(0, [])
        return result
