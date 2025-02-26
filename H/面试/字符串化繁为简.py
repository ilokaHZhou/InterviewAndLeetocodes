from collections import deque
from typing import List, Set

def main():
    # 创建一个输入函数，用于读取用户输入
    input_string = input()
    # 创建一个列表，用于存储最终的输出结果
    output_string_builder = []
    # 创建一个双端队列对象，用于存储等价集合
    equivalent_sets = deque()

    # 用于判断当前是否在括号内部的标志变量
    is_inside_parentheses = False

    # 遍历输入字符串的每个字符
    for current_char in input_string:
        # 如果当前字符是左括号'('，则表示进入了括号内部
        if current_char == '(':
            is_inside_parentheses = True
            # 创建一个新的等价集合，并将其添加到双端队列中
            equivalent_sets.append(set())
        # 如果当前字符是右括号')'，则表示离开了括号内部
        elif current_char == ')':
            is_inside_parentheses = False
            # 如果最后一个等价集合为空集合，则将其从双端队列中移除
            if len(equivalent_sets[-1]) == 0:
                equivalent_sets.pop()
        # 如果当前字符既不是左括号也不是右括号
        else:
            # 如果当前不在括号内部，则直接将字符添加到输出结果中
            if not is_inside_parentheses:
                output_string_builder.append(current_char)
            # 如果当前在括号内部，则将字符添加到最后一个等价集合中
            else:
                equivalent_sets[-1].add(current_char)

    # 用于判断是否进行了合并操作的标志变量
    merged = True
    # 循环执行合并操作，直到没有可以合并的等价集合为止
    while merged:
        merged = False
        # 遍历等价集合双端队列中的每个等价集合
        for i in range(len(equivalent_sets)):
            for j in range(i + 1, len(equivalent_sets)):
                can_combine = False
                # 遍历字母'a'到'z'，判断两个等价集合是否可以合并
                for c in range(ord('a'), ord('z') + 1):
                    uppercase_c = chr(c - 32)
                    if (chr(c) in equivalent_sets[i] or uppercase_c in equivalent_sets[i]) and (chr(c) in equivalent_sets[j] or uppercase_c in equivalent_sets[j]):
                        can_combine = True
                        break
                # 如果可以合并，则将第二个等价集合中的元素合并到第一个等价集合中，并从双端队列中移除第二个等价集合
                if can_combine:
                    equivalent_sets[i].update(equivalent_sets[j])
                    del equivalent_sets[j]
                    merged = True
                    break
            if merged:
                break

    # 对每个等价集合进行处理，将等价集合中的字符替换为集合中的第一个字符
    for eq in equivalent_sets:
        first_char = min(eq)
        for i in range(len(output_string_builder)):
            if output_string_builder[i] in eq:
                output_string_builder[i] = first_char

    # 将字符列表转换为字符串
    result_string = ''.join(output_string_builder)

    # 如果结果字符串为空，则返回"0"，否则返回结果字符串
    final_result = "0" if len(result_string) == 0 else result_string
    print(final_result)

if __name__ == "__main__":
    main()