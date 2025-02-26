# 定义 TrieNode 类，每个节点包含一个布尔值 is_word 和一个 TrieNode 类型的数组 children
class TrieNode:
    def __init__(self):
        self.is_word = False  # 标记该节点是否为一个单词的结束
        self.children = [None] * 26  # 存储子节点的数组，每个元素对应一个字母

# 创建 Trie 的根节点
root = TrieNode()

# 插入方法，用于向 Trie 中插入一个单词
def insert(word):
    node = root  # 从根节点开始
    for c in word:
        index = ord(c) - ord('a')  # 计算当前字符对应的索引
        # 如果当前字符对应的子节点为空，则创建一个新的子节点
        if node.children[index] is None:
            node.children[index] = TrieNode()
        # 移动到下一个子节点
        node = node.children[index]
    # 标记当前节点为一个单词的结束
    node.is_word = True

# 输入句子，并将其转换为小写
sentence = input().lower()
# 输入字典，字典中的单词以逗号分隔
dictionary = input().split(",")
for word in dictionary:
    insert(word.lower())  # 将字典中的每个单词插入到 Trie 中

result = []  # 存储结果
i = 0
# 遍历句子中的每个字符
while i < len(sentence):
    # 如果当前字符不是字母，则直接将其添加到结果中
    if not sentence[i].isalpha():
        result.append(sentence[i])
        i += 1
        continue
    j = len(sentence)
    # 从句子的末尾开始，寻找以 i 为起点的最长的在字典中存在的单词
    while j > i:
        node = root
        is_word = True
        for k in range(i, j):
            # 如果当前字符不是字母，或者在 Trie 中不存在对应的子节点，则说明当前的字符串不是一个单词
            if not sentence[k].isalpha() or node.children[ord(sentence[k]) - ord('a')] is None:
                is_word = False
                break
            # 移动到下一个子节点
            node = node.children[ord(sentence[k]) - ord('a')]
        # 如果找到了一个单词，则结束循环
        if is_word and node.is_word:
            break
        # 如果没有找到单词，则缩短当前的字符串
        j -= 1
    # 如果没有找到单词，则将当前字符作为一个单独的单词添加到结果中
    if j == i:
        result.append(sentence[i])
        i += 1
    else:
        # 如果找到了单词，则将该单词添加到结果中
        result.append(sentence[i:j])
        i = j

# 输出结果，单词之间以逗号分隔
print(",".join(result))