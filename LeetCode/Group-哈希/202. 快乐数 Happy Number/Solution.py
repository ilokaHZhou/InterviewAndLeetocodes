# 由于可以无限循环，用set来记录每个变换后的数字
# 不是快乐数的变着变着就会重复自身陷入循环，始终变不到1，快乐数的最终会变成1
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while n not in record:
            record.add(n)
            new_num = 0
            n_str = str(n)
            for i in n_str:
                new_num = new_num + int(i) ** 2
            if new_num == 1:
                return True
            else:
                n = new_num
        return False