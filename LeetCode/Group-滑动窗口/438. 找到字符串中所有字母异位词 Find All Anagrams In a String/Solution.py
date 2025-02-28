class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        # 如果p比s长，直接返回空数组
        if s_len < p_len:
            return []

        result = []

        # 初始化两个数组一个记录s里每个字母数目，一个记录p里每个字母数目
        s_freq = [0] * 26
        p_freq = [0] * 26

        # 根据p的长度分别初始化p里的字母计数，和s滑动窗口起始位置的字母计数
        for i in range(p_len):
            s_freq[ord(s[i]) - ord('a')] += 1 
            p_freq[ord(p[i]) - ord('a')] += 1

        # 如果此时就相等，index 0加入result
        if s_freq == p_freq:
            result.append(0)

        # 在s上滑动窗口的起始点，每向右滑动一位，新字母频率加一，左侧滑出的旧字母频率减一
        # i是滑出那一位，i + 1是滑动后窗口的起始点
        for i in range(s_len - p_len):
            s_freq[ord(s[i]) - ord('a')] -= 1
            s_freq[ord(s[i + p_len]) - ord('a')] += 1

            if s_freq == p_freq:
                result.append(i + 1)

        return result