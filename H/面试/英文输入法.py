import string

sentence = input() # 输入一段由英文单词word和标点符号组成的语句
prefix = input() # 输入一个英文单词前缀
sentence = sentence.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))) # 将标点符号替换为空格
word_set = set(sentence.split()) # 存储单词的集合，自动去重且按照字典序排序
ans = ''
for s in sorted(word_set): # 遍历单词集合
    if s.startswith(prefix): # 如果单词以前缀开头
        ans += s + ' ' # 将单词加入答案字符串
if ans: # 如果答案字符串不为空
    print(ans) # 输出单词序列
else:
    print(prefix) # 否则输出前缀