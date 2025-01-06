'''
由于只能用常数额外空间，因此使用三指针：

1. write_index 负责记录字符和它们的count的位置
2. char_index 负责记录每个不同字符的起始位置
3. i 负责遍历数组

计算出count后使用短除法诸位获取数字，再用双指针reverse将位数按前后顺序反转写入数组
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        def reverse(left: int, right: int) -> None:
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        write_index = 0
        char_index = 0
        n = len(chars)
        for i in range(n):
            if i == n - 1 or chars[i] != chars[i + 1]:
                chars[write_index] = chars[i]
                write_index += 1
                num = i - char_index + 1
                if num > 1:
                    anchor = write_index
                    while num > 0:
                        chars[write_index] = str(num % 10)
                        write_index += 1
                        num = num // 10
                    reverse(anchor, write_index - 1)

                char_index = i + 1
        return write_index