class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        result = -1
        while left <= right:
            # 不断更新中间和左右两个边界
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            # 是否需要特判 nums[mid]=target 的情况？可以，但没必要
        # 如果需要插入，插入位置也是最后查询位置的left index
        return left