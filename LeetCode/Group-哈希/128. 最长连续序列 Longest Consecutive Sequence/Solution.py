# 用set去除重复数字，然后检查每个数字是否为已知数列的一部分，如果不是，重置current数列长度，
# 并依次按照连续下一个数字找新数列的最大长度与当前最长数列比较
# 当有一个数是连续数列的第一个数才进入循环
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest