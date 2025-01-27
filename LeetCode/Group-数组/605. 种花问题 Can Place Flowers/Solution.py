# 前后补0作为虚拟边界，检查是否有三个连续的0组成的坑位，有的话就种下一颗
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) -1):
            if (flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0):
                flowerbed[i] = 1 
                n -= 1
                if n == 0:
                    return True
            
        return False
