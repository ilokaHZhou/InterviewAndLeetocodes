# 如果两个字符串有最大公因子那么str1+str2和str2+str1一定是一样的，因为它们由同样的重复子串构成
# 因此先判断，然后用两者的长度，用辗转相除法计算公因数，再在原字符串中截取对应长度的子串
# 辗转相除法/欧几里得算法就是互相除，除不尽了取余数交换继续除取余，（两个整数的最大公约数等于其中较小的数和两数相除余数的最大公约数。）

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]