package Java;

import java.util.Arrays;
import java.util.Comparator;

/**
 * @see <a href="https://leetcode-cn.com/problems/largest-number/"></a>
 * 本质还是对数组进行排序，不过排序的规则变成按位进行排序了
 */
class Solution0179 {

    public String largestNumber(int[] nums) {
        StringBuilder stringBuilder = new StringBuilder();
        Arrays.stream(nums).boxed().sorted(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                String s1 = o1.toString();
                String s2 = o2.toString();
                for (int i = 0; ; i++) {
                    if (i > s1.length() && i > s2.length()) {
                        return s1.length() - s2.length();
                    }
                    char c1;
                    char c2;
                    if (i > s1.length() - 1) {
                        c1 = s1.charAt(i % s1.length());
                    } else {
                        c1 = s1.charAt(i);
                    }
                    if (i > s2.length() - 1) {
                        c2 = s2.charAt(i % s2.length());
                    } else {
                        c2 = s2.charAt(i);
                    }

                    // System.out.println("==="+c1+"----"+c2);

                    if (c1 != c2) {
                        return c2 - c1;
                    }
                }
            }
        }).forEach(stringBuilder::append);
        String result = stringBuilder.toString();
        if (result.charAt(0) == '0') {
            return "0";
        }
        return result;
    }


    public static void main(String[] s) throws Exception {
        Solution0179 Solution0179 = new Solution0179();
        // System.out.println(Solution0179.largestNumber(new int[]{34323, 3432}));
        // System.out.println(Solution0179.largestNumber(new int[]{111311, 1113}));
        // System.out.println(Solution0179.largestNumber(new int[]{5, 3, 30, 34, 9}));
        // System.out.println(Solution0179.largestNumber(new int[]{0, 0}));
        System.out.println(Solution0179.largestNumber(new int[]{8247, 824}));
    }
}