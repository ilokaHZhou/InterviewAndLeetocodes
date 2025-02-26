import sys

def main():
    # 输入每块芯片的容量和板卡上芯片的数量
    chip_capacity = int(input())  # 每块芯片的容量
    chip_count = int(input())      # 板卡上芯片的数量

    # 输入用户配置序列
    sequence = input()  # 用户配置序列

    # 初始化每块板卡的总容量
    board_card = [chip_capacity * 1.25] * chip_count

    # 遍历用户配置序列，按照芯片编号从小到大分配所需资源
    for config in sequence:
        if config == 'A':
            need = 1.25 * 1  # 1.25G
        elif config == 'B':
            need = 1.25 * 2  # 2.5G
        elif config == 'C':
            need = 1.25 * 8  # 10G
        else:
            continue  # 如果是未知配置，跳过

        # 分配资源
        for j in range(chip_count):
            if board_card[j] >= need:
                board_card[j] -= need  # 减去所需容量
                break

    # 输出每块芯片的占用情况
    for i in range(chip_count):
        un_used = int(board_card[i] / 1.25)  # 计算未使用的容量
        used = chip_capacity - un_used  # 计算已使用的容量

        # 构造字符串表示每块芯片的占用情况
        result = '1' * used + '0' * un_used  # 使用 '1' 表示已占用，'0' 表示未占用
        print(result)  # 输出结果

if __name__ == "__main__":
    main()