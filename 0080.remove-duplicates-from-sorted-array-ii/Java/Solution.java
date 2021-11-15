package Java;

import java.util.Arrays;

/**
 * @see <a href="https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/"></a>
 * 考虑到从前往后的遍历会造成后面重复的元素多次拷贝，所以从后往前遍历
 * 此方法时间复杂度较高，故使用快慢指针
 */
class Solution0080 {

    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2) {
            return nums.length;
        }
        int fastIndex = 2;
        int slowIndex = 2;
        while (fastIndex < nums.length) {
            if (nums[slowIndex - 2] != nums[fastIndex]) {
                nums[slowIndex] = nums[fastIndex];
                slowIndex++;
            }
            fastIndex++;
        }
        return slowIndex;
    }

    public static void main(String[] s) throws Exception {
        int[] nums = new int[]{1, 1, 1, 2, 2, 3};
        // int[] nums = new int[]{0, 0, 1, 1, 1, 1, 2, 3, 3};
        // int[] nums = new int[]{-1, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4};
        Solution0080 solution0080 = new Solution0080();
        System.out.println(solution0080.removeDuplicates(nums));
        System.out.println(Arrays.toString(nums));

    }
}