"""
使用 单调队列 来解决这个问题。单调队列的核心思想是维护一个队列，队列中的元素是单调递减的，队首元素始终是当前窗口的最大值。

初始化：

    使用一个双端队列 deque 来存储数组的索引。

    使用一个列表 result 来存储每个窗口的最大值。（i - k + 1）是窗口左边界的索引

遍历数组：

    对于每个元素 nums[i]：

        如果队列不为空且队首元素不在当前窗口范围内（即 deque[0] < i - k + 1），则移除队首元素。

        如果队列不为空且当前元素 nums[i] 大于队尾元素，则移除队尾元素，直到队列为空或队尾元素大于当前元素。

        将当前元素的索引 i 加入队尾。

        如果当前窗口已经形成（即 i >= k - 1），则将队首元素对应的值加入 result。

如果比喻窗口是一个公司的HC，数组里每个元素是一个候选人的能力值
那么优先队列队尾能力比不过新进年轻人的统统删掉，队头超出年龄区间的删掉（无论能力多少）
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        # 使用双端队列存储索引
        deque_window = deque()
        result = []

        for i in range(len(nums)):
            # 移除不在当前窗口范围内的队首元素
            if deque_window and deque_window[0] < i - k + 1:
                deque_window.popleft()

            # 移除队尾小于当前元素的元素
            while deque_window and nums[i] > nums[deque_window[-1]]:
                deque_window.pop()

            # 将当前元素的索引加入队尾
            deque_window.append(i)

            # 如果窗口已经形成，开始逐步将队首元素对应的值加入结果，比如k=3，那么从索引2开始
            if i - k + 1 >= 0:
                result.append(nums[deque_window[0]])

        return result