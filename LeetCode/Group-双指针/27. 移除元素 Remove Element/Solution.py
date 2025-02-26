# 快指针：寻找新数组的元素 ，新数组就是不含有目标元素的数组
# 慢指针：指向更新 新数组下标的位置

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针
        fast = 0  # 快指针
        slow = 0  # 慢指针
        size = len(nums)
        while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast] # 跳过当前元素 -> 把后一个元素挪到前一个元素位置，当有元素被跳过，之后的所有元素遍历时都要移动位置
                slow += 1 # 只有不等于目标值时更新slow index
            fast += 1
        return slow