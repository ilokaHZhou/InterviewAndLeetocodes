puzzle_words = input().split(",")
word_bank = input().split(",")

# 用于存储匹配到的正确单词列表
matched_words = []

# 遍历每个谜面
for puzzle_word in puzzle_words:
    # 将谜面中的字符去重并排序
    sorted_puzzle_word = "".join(sorted(set(puzzle_word)))
    # 标记是否找到匹配的谜底
    found = False

    # 遍历每个谜底
    for word in word_bank:
        # 将谜底中的字符去重并排序
        sorted_word = "".join(sorted(set(word)))

        # 判断谜底是否与谜面匹配
        if sorted_puzzle_word == sorted_word:
            # 将匹配到的谜底添加到结果列表中
            matched_words.append(word)
            # 标记为已找到匹配的谜底
            found = True

    # 如果没有找到匹配的谜底，将"not found"添加到结果列表中
    if not found:
        matched_words.append("not found")

# 输出匹配到的正确单词列表，以","分隔
print(",".join(matched_words))