# 用双指针从两侧向中间遍历，容积 = 两个指针指向的数字中较小值∗指针之间的距离
# 因此需要不断更新两个指针指向的更小的那个值，再找最大的容积
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        most_contained = 0
        while left < right:
            val_right = height[right]
            val_left = height[left]
            water_contained = min(val_left, val_right) * (right - left)
            if val_right > val_left:
                left += 1
            else:
                right -= 1
            most_contained = max(water_contained, most_contained)
        return most_contained