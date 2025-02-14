# 保留字母和数字字符，然后可以将字符串翻转然后逐个比较，也可以双指针一个从头一个从尾while left < right遍历比较
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]
