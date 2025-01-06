class Solution:
    def countWays(self, nums: List[int]) -> int:
        result = 2 # 全选和全不选的2种边际情况
        selected = 0
        nums = sorted(nums) # 遇事不决先排序
        if nums[0] == 0: # 当有值为0的元素，则边际情况少一种
            result = 1
        for i in range(1, len(nums)): # 遍历全班，每次多选一人，
            selected += 1
            if selected > nums[i-1] and selected < nums[i]: # 看选中的学生数是否能够插空在已选择和未选择的学生的值中间，来判定是否为可用的分组
                result += 1
        return result