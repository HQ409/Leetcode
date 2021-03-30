package Java;

/**
 * @see <a href="https://leetcode-cn.com/problems/search-a-2d-matrix/"></a>
 * 74. 搜索二维矩阵
 */
class Solution74 {
    public boolean searchMatrix(int[][] matrix, int target) {
        //二维矩阵简化为一维数组进行二分查找
        int length = matrix[0].length;
        int width = matrix.length;
        int start = 0;
        int end = length * width-1;
        int middle = end / 2;
        while (start <= middle && middle <= end) {
            middle = start + (end - start) / 2;
            if (start == middle || middle == end) {
                return getValue(matrix, start) == target || getValue(matrix, end) == target;
            }
            int middleValue = getValue(matrix, middle);
            if (middleValue > target) {
                end = middle;
            } else if (middleValue < target) {
                start = middle;
            } else {
                return true;
            }
        }
        return false;
    }

    int getValue(int[][] matrix, int index) {
        int length = matrix[0].length;
        return matrix[index / length][index % length];
    }

    public static void main(String[] s) throws Exception {
        Solution74 Solution74 = new Solution74();
        // int[][] matrix = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
        System.out.println(Solution74.searchMatrix(new int[][]{{1}, {60}}, 1));
        System.out.println(Solution74.searchMatrix(new int[][]{{1}, {60}}, 2));
        System.out.println(Solution74.searchMatrix(new int[][]{{1}}, 1));
        System.out.println(Solution74.searchMatrix(new int[][]{{1}}, 2));
        System.out.println(Solution74.searchMatrix(new int[][]{{1,3}}, 1));
        System.out.println(Solution74.searchMatrix(new int[][]{{1,3}}, 3));
        System.out.println(Solution74.searchMatrix(new int[][]{{1,3}}, 2));
        System.out.println(Solution74.searchMatrix(new int[][]{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}, 1));
        System.out.println(Solution74.searchMatrix(new int[][]{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}, 3));
        System.out.println(Solution74.searchMatrix(new int[][]{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}, 5));
        System.out.println(Solution74.searchMatrix(new int[][]{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}, 7));
        System.out.println(Solution74.searchMatrix(new int[][]{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}, 2));
        System.out.println(Solution74.searchMatrix(new int[][]{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}, 60));
    }
}