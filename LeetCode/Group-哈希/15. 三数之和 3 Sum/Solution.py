"""
1. 哈希解法

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # 先排序，这样如果所有元素大于等于0，就凑不成三元组，不用往下了
        n = len(nums)
        # 找出a + b + c = 0
        # a = nums[i], b = nums[j], c = -(a + b)
        for i in range(n):
            # 排序之后如果第一个元素已经大于零，那么不可能凑成三元组
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]: #三元组元素a去重
                continue

            record = {} # 用字典结合哈希特性
            for j in range(i + 1, n): # j从i+1开始
                if j > i + 2 and nums[j] == nums[j - 1] == nums[j - 2]: #三元组元素b去重
                    continue
                c = 0 - nums[i] - nums[j]
                if c in record:
                    result.append([nums[i], nums[j], c])
                    record.pop(c) #三元组元素c去重，用过的元素不能再用了
                else:
                    record[nums[j]] = j
        return result


2. 双指针解法：双指针要先排序是为了left right两个指针移动方向向左变小，向右变大
    并且由于自小向大排序只有(a,b,c)这个顺序会被枚举到，而(b,a,c)、(c,b,a)等等这些不会，实现结果去重
    双指针的a,b,c分别为nums[i], nums[left], nums[right]
    输出元组中有元素可以被重用，但整个三元组不是重复的
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            # 如果第一个元素已经大于0，不需要进一步检查
            if nums[i] > 0:
                return result
            
            # 跳过相同的元素以避免重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]
                
                if sum_ < 0:
                    left += 1 # 最小值往右挪一个，让sum稍微变大一点
                elif sum_ > 0:
                    right -= 1 # 最大值往左挪一个，让sum稍微变小一点
                else:
                    result.append([nums[i], nums[left], nums[right]]) # 找到符合条件的元组
                    
                    # 左右指针变化前都跳过相同的元素以避免重复
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    # 找到和为0的元组后左右边界都更新到下一位    
                    right -= 1
                    left += 1
                    
        return result