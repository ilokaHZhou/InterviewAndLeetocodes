class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        n = len(nums)
        result = []

        def backTrack(first_index):
            # 所有数都填完了
            if first_index == n:
                result.append(nums[:])
            else:
                for i in range(first_index, n):
                    # 动态维护数组
                    nums[first_index], nums[i] = nums[i], nums[first_index]
                    # 继续递归填下一个数
                    backTrack(first_index + 1)
                    # 撤销操作
                    nums[first_index], nums[i] = nums[i], nums[first_index]

        
        backTrack(0)
        return result