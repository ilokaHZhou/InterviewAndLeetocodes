class Solution:
    @staticmethod
    def binarySearch(arr, target, left, right): # 递归体
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:  # 递归终止条件
            return mid
        elif arr[mid] > target:
            return Solution.binarySearch(arr, target, left, mid - 1)  # 左
        else: 
            return Solution.binarySearch(arr, target, mid + 1, right) # 右

    def search(self, nums: List[int], target: int) -> int: # 递归解法
        if (nums):
            return Solution.binarySearch(nums, target, 0, len(nums) - 1)
        return -1
    

'''
不带static method的写法

class Solution:
    def binarySearch(self, arr, target, left, right): # 递归体
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return self.binarySearch(arr, target, left, mid - 1)
        else: 
            return self.binarySearch(arr, target, mid + 1, right)

    def search(self, nums: List[int], target: int) -> int: # 递归解法
        if (nums):
            return self.binarySearch(self, nums, target, 0, len(nums) - 1)
        return -1

'''