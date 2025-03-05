class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        n = len(s)
        left = right = result =0
        while right < n:
            new_char = s[right]
             # 如果新字符在字串中已经出现过，缩短左边界并从set移除左侧元素，直到从左边界开始到右边界的连续子串中完全没有重复的新char
            while new_char in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(new_char)
            right += 1
            result = max(result, right - left)
        return result