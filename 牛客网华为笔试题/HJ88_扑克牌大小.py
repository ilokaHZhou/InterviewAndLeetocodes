def compare_poker(poker1, poker2):
    # 定义扑克牌的权重
    weight = {'3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6,
              '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12, '2': 13,
              'joker': 14, 'JOKER': 15}
    # 判断是否为炸弹
    def is_bomb(poker):
        return len(poker) == 4 and len(set(poker)) == 1
    # 判断是否为王炸
    def is_joker_bomb(poker):
        return len(poker) == 2 and set(poker) == {'joker', 'JOKER'}
    # 判断牌型是否合法
    def is_valid(poker):
        return len(poker) in {1, 2, 3, 4, 5}
    # 判断牌型是否一致
    if len(poker1) != len(poker2):  # 如果牌型不一致
        if is_joker_bomb(poker1):  # 如果 poker1 是王炸
            return ' '.join(poker1)
        if is_joker_bomb(poker2):  # 如果 poker2 是王炸
            return ' '.join(poker2)
        if is_bomb(poker1):  # 如果 poker1 是炸弹
            return ' '.join(poker1)
        if is_bomb(poker2):  # 如果 poker2 是炸弹
            return ' '.join(poker2)
        return 'ERROR'  # 否则返回错误
    # 比较牌型
    if not is_valid(poker1) or not is_valid(poker2):  # 如果牌型不合法
        return 'ERROR'
    # 比较单张牌的大小
    if len(poker1) == 1:
        return ' '.join(poker1) if weight[poker1[0]] > weight[poker2[0]] else ' '.join(poker2)
    # 比较对子、三张、顺子、炸弹的大小
    return ' '.join(poker1) if weight[poker1[0]] > weight[poker2[0]] else ' '.join(poker2)

# 输入处理
poker1, poker2 = input().split('-')
poker1_list = poker1.split(' ')
poker2_list = poker2.split(' ')

# 调用函数并输出结果
print(compare_poker(poker1_list, poker2_list))