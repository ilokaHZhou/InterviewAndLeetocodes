# 数组为有序数组
# 数组中无重复元素

# 左闭右闭区间 while循环查找

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 定义target在左闭右闭的区间里，[left, right]

        while left <= right:
            mid = left + (right - left) // 2

            if target < nums[mid]: # 左区间
                right = mid - 1 # 因为左闭右闭所以右边界不能等于mid
            elif target > nums[mid]: # 右区间
                left = mid + 1
            else:
                return mid
            # 如果没找到 right会小于left 或者 left会大于right
        return -1