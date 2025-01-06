# 双指针遍历两个数组，谁数小谁添加进结果数组
# 也可从最后反向遍历数组，谁大谁放到nums1最后，这样不需额外空间，空间复杂度进一步降到O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        i = j = 0
        while i < m or j < n:
            if i == m:
                result.append(nums2[j])
                j += 1
            elif j == n:
                result.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                result.append(nums2[j])
                j += 1
            else:
                result.append(nums1[i])
                i += 1
        nums1[:] = result