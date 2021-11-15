package Java;

import java.util.Arrays;

/**
 * @see <a href="https://leetcode-cn.com/problems/merge-sorted-array/"></a>
 * 因为num1后面是空白，故从后往前填充
 */
class Solution0088 {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int index1 = m - 1;
        int index2 = n - 1;
        int finalIndex = m + n - 1;
        while (index1 >= 0 && index2 >= 0) {
            if (nums1[index1] >= nums2[index2]) {
                nums1[finalIndex] = nums1[index1];
                index1--;
            } else {
                nums1[finalIndex] = nums2[index2];
                index2--;
            }
            finalIndex--;
        }
        while (index1 >= 0) {
            nums1[finalIndex] = nums1[index1];
            index1--;
            finalIndex--;
        }
        while (index2 >= 0) {
            nums1[finalIndex] = nums2[index2];
            index2--;
            finalIndex--;
        }
    }

    public static void main(String[] s) throws Exception {
        Solution0088 Solution0088 = new Solution0088();

        // int[] nums1 = new int[]{1, 2, 3, 0, 0, 0};
        // int[] nums2 = new int[]{2, 5, 6};
        // Solution0088.merge(nums1, 3, nums2, 3);

        int[] nums1 = new int[]{0};
        int[] nums2 = new int[]{1};
        Solution0088.merge(nums1, 0, nums2, 1);

        System.out.println(Arrays.toString(nums1));

    }
}