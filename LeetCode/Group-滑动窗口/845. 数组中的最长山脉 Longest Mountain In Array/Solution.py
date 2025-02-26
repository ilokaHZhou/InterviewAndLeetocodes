# 由于有平地不算山脉，因此用上下山的状态来更新滑动窗口边界更为直观
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left = right = longestHill = status = 0
        while right < len(arr) - 1:
            if status == 0: # 遍历到第一个谷底前
                if arr[right] < arr[right + 1]:
                    status = 1
                    left = right
            elif status == 1: # status等于1时，表示正在爬山
                if arr[right] > arr[right + 1]: # 越过山顶时，进入下山状态
                    status = 2
                elif arr[right] == arr[right + 1]: # 遇到平地重新计算爬山状态
                    status = 0
            else: # 此时status等于2，在下山状态
                if arr[right] <= arr[right + 1]: # 下山遇到谷底，先结算山脉长度
                    longestHill = max(right - left + 1, longestHill)
                    if arr[right] < arr[right + 1]: # 再根据后面是新的山脉还是平地决定下一个状态
                        status = 1
                        left = right
                    else:
                        status = 0
            right += 1
        if status == 2: # 遍历到数组最后都是下山，因为右侧边界没有谷底判定，此时需要额外判定一下max山脉长度
            longestHill = max(right - left + 1, longestHill)
        return longestHill