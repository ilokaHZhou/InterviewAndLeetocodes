import sys

def getNextWord(wordList, suffix):
    # 创建一个映射表，键为单词的首字母，值为以该首字母开头的单词列表
    map = {}
    
    # 遍历单词列表，将单词按首字母分类存储到映射表中
    for word in wordList:
        firstChar = word[0]
        tempList = map.get(firstChar, [])
        tempList.append(word)
        map[firstChar] = tempList
    
    # 初始化最长长度和字典序最小的单词
    maxLength = 0
    minWord = ""
    
    # 获取以suffix为首字母的单词列表
    tempList = map.get(suffix)
    
    # 如果列表为空，则没有符合条件的单词，返回None
    if not tempList:
        return None
    
    # 遍历单词列表，找到最长长度和字典序最小的单词
    for word in tempList:
        if len(word) > maxLength or (len(word) == maxLength and word < minWord):
            maxLength = len(word)
            minWord = word
    
    # 如果最小单词为空，则没有符合条件的单词，返回None
    return minWord if minWord else None

if __name__ == "__main__":
    # 输入起始单词的索引
    startIndex = int(input())
    
    # 输入单词的个数
    number = int(input())
    
    # 创建一个存储单词的列表
    wordList = [input().strip() for _ in range(number)]

    
    # 初始化结果字符串为起始单词
    result = wordList[startIndex]
    
    # 从列表中移除起始单词
    wordList.pop(startIndex)
    
    # 获取下一个符合条件的单词
    nextWord = getNextWord(wordList, result[-1])
    
    # 循环直到没有符合条件的单词为止
    while nextWord:
        # 拼接下一个单词到结果字符串
        result += nextWord
        
        # 从列表中移除已使用的单词
        wordList.remove(nextWord)
        
        # 获取下一个符合条件的单词
        nextWord = getNextWord(wordList, result[-1])
    
    # 输出最终拼接的单词串
    print(result)
