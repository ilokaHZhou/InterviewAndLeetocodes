"""
使用额外的数组的话，新建数组，将下标为i的元素放到（i+k）mod n的位置，再将新数组拷贝到原数组，这样空间复杂度是O（n）
如果不使用额外空间，可以翻转数组，将前n-k+1个元素翻过来，再把后k个元素翻过来
k = 3
1 2 3 4 5 6 7
output = 
5 6 7 1 2 3 4
注意是向右轮转而不是向左
可以先整体翻转
7 6 5 4 3 2 1
翻前k个
5 6 7 4 3 2 1
再翻后面的
5 6 7 1 2 3 4

k会大于n所以，k要mod n


"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        reverse(0, n - 1)
        reverse(0, k%n - 1)
        reverse(k%n, n - 1)
        