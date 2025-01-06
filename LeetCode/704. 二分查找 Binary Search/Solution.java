class Solution {
    public int search(int[] nums, int target) {
        int i = 0, j = nums.length - 1;
        while(i <= j) {
            int m = (i + j) / 2;
            int midValue = nums[m];
            if (target < midValue)
                j = m - 1;
            else if (target > midValue)
                i = m + 1;
            else
                return m;
        }
        return -1;
        
    }
}



class Solution2 {
    public int search(int[] nums, int target) {
        if (nums.length > 0)
            return binarySearch(nums, target, 0, nums.length - 1);
        return -1;
    }

    public static int binarySearch(int[] arr, int target, int left, int right) {
        if (left > right)
            return -1;
        int m = (left + right) / 2;
        int midValue = arr[m];
        if (target == midValue)
            return m;
        else if (target < midValue)
            return binarySearch(arr, target, left, m - 1);
        else
            return binarySearch(arr, target, m + 1, right);
    }
}