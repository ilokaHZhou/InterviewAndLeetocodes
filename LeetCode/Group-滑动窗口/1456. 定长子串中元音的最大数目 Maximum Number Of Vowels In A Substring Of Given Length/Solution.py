# 滑动窗口，如果向右侧移动窗口，如果一进一出都是元音则抵消，如果进是元音出是其他则加一，反之减一
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(ch):
            return int(ch in 'aeiou')
        n = len(s)
        vowel_count = sum(1 for i in range(k) if isVowel(s[i]))
        result = vowel_count
        for i in range(k, n):
            vowel_count += isVowel(s[i]) - isVowel(s[i - k])
            result = max(result, vowel_count)
        return result
