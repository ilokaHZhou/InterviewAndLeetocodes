"""
如果已知有一个 x,x+1,x+2,⋯,x+y 的连续序列，而我们却重新从 x+1，x+2 或者是 x+y 处开始尝试匹配，那么得到的结果肯定不会优于枚举 x 为起点的答案，因此我们在外层循环的时候碰到这种情况跳过即可。
用set去除重复数字，然后检查每个数字是否为已知数列的一部分，如果不是，重置current数列长度，
并依次按照连续下一个数字找新数列的最大长度与当前最长数列比较
当有一个数是连续数列的第一个数才进入循环
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums) # 包含所有nums里字母的集合

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest