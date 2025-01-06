# 同样要求一一映射，用两个相互映射的哈希表来判断
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ch2word = dict()
        word2ch = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for ch, word in zip(pattern, words):
            if (ch in ch2word and ch2word[ch] != word) or (word in word2ch and word2ch[word] != ch):
                return False
            ch2word[ch] = word
            word2ch[word] = ch
        return True
