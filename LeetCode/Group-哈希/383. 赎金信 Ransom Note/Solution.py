class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransomNote:
            ransom_count[ord(c) - ord('a')] += 1
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        # 检查是否ransom里出现的字符都在magazine里有, 且数量不多于magazine提供的
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))