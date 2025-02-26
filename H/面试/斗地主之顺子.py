# 导入Python标准库
from collections import deque

# 定义一个字典，用于映射扑克牌的牌面到数字，方便比较大小
CARD_TO_NUMBER = {
    '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
    'A': 14, '2': 16
}

 
# 使用input函数读取一行输入，并用split方法按空格分割字符串，得到牌面数组
cards = input().split()
# 根据牌面大小对牌进行排序
cards.sort(key=lambda x: CARD_TO_NUMBER[x])

straights = []  # 存储所有可能的顺子序列
current_straight = deque([cards[0]])  # 初始化当前顺子序列，使用deque提高效率
straights.append(current_straight)  # 将当前顺子序列添加到列表中

# 遍历输入的牌，从第二张牌开始
for card in cards[1:]:
    added = False  # 标记当前牌是否已被添加到某个顺子中

    # 尝试将当前牌加入到已存在的顺子序列中
    for straight in straights:
        # 判断当前牌是否可以追加到顺子末尾
        if CARD_TO_NUMBER[card] - CARD_TO_NUMBER[straight[-1]] == 1:
            straight.append(card)
            added = True
            break
    
    # 如果当前牌没有加入到任何顺子中，创建一个新的顺子序列
    if not added:
        new_straight = deque([card])
        straights.append(new_straight)

# 筛选出长度至少为5的有效顺子序列
valid_straights = [list(straight) for straight in straights if len(straight) >= 5]

# 如果没有找到有效的顺子序列，输出"No"
if not valid_straights:
    print("No")
else:
    # 对所有有效的顺子进行排序，并输出
    valid_straights.sort(key=lambda x: CARD_TO_NUMBER[x[0]])
    for straight in valid_straights:
        print(" ".join(straight))
