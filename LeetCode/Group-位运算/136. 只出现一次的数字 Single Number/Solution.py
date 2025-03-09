"""
官方解是用位运算，对于这道题，可使用异或运算 ⊕异或运算有以下三个性质。

1. 任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0=a。
2. 任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
3. 异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。

根据性质 3，数组中的全部元素的异或运算结果可以写成所有元素的异或运算的结果
相等的数算完得0，0和唯一的那个数做完运算得到它本身

class Solution {
    public int singleNumber(int[] nums) {
        int single = 0;
        for (int num : nums) {
            single ^= num;
        }
        return single;
    }
}

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = set()
        for item in nums:
            if item not in mapping:
                mapping.add(item)
            else:
                mapping.remove(item)
        return list(mapping)[0]