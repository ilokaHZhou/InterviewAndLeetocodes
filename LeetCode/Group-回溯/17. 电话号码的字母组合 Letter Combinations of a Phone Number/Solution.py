class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 数字到字母的映射
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backTrack(index, current_combinations):
            # 如果当前组合的长度等于输入字符串的长度，将其加入结果列表
            if index == len(digits):
                result.append(''.join(current_combinations))
            else:
                number = digits[index]
                letters = digit_to_letters[number]

                # 遍历当前数字对应的每个字母
                for letter in letters:
                    # 将当前字母加入组合
                    current_combinations.append(letter)
                    # 递归处理下一个数字
                    backTrack(index + 1, current_combinations)
                    # 回溯，移除当前字母
                    current_combinations.pop()
        
        backTrack(0, [])

        return result