from typing import List, Tuple

def main():
    n = int(input())  # 输入猜测的次数

    # 存储所有猜测的数字和提示结果
    guess_infos = [tuple(input().split()) for _ in range(n)]

    valid_count = 0  # 记录符合条件的答案数量
    valid_answer = ""  # 存储符合条件的答案

    # 遍历所有可能的四位数
    for num in range(10000):
        answer = f"{num:04d}"  # 将数字格式化为四位数字符串
        is_valid = True  # 标记当前答案是否有效

        # 遍历每个猜测的数字和结果
        for guess, expect_result in guess_infos:
            count_a = 0  # 记录数字和位置都正确的个数
            count_b = 0  # 记录数字正确但位置不正确的个数

            answer_arr = [0] * 10  # 存储答案中每个数字出现的次数
            guess_arr = [0] * 10  # 存储猜测中每个数字出现的次数

            # 遍历每个位置
            for i in range(len(guess)):
                c1_int = int(guess[i])  # 获取猜测中该位置上的数字
                c2_int = int(answer[i])  # 获取答案中该位置上的数字

                if c1_int == c2_int:
                    count_a += 1  # 如果数字和位置都正确，countA+1
                else:
                    guess_arr[c1_int] += 1  # 在 guessArr 中记录该数字出现的次数
                    answer_arr[c2_int] += 1  # 在 answerArr 中记录该数字出现的次数

            count_b = sum(min(answer_arr[i], guess_arr[i]) for i in range(10))  # 计算数字正确但位置不正确的个数

            real_result = f"{count_a}A{count_b}B"  # 根据猜测和答案计算真实结果

            if real_result != expect_result:
                is_valid = False  # 如果真实结果和猜测结果不一致，标记当前答案为无效
                break

        if is_valid:
            valid_count += 1  # 如果当前答案有效，更新符合条件的答案数量
            valid_answer = answer  # 更新符合条件的答案

            if valid_count > 1:
                break  # 如果符合条件的答案数量大于1，跳出循环

    if valid_count != 1:
        print("NA")  # 如果符合条件的答案不唯一，输出 NA
    else:
        print(valid_answer)  # 如果符合条件的答案唯一，输出答案

if __name__ == "__main__":
    main()
