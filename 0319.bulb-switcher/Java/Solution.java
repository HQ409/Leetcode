package Java;

import java.util.Arrays;

/**
 * @see <a href="https://leetcode-cn.com/problems/bulb-switcher/"></a>
 * 笨办法:挨个输出数组，但是由于n最大值为99999999，内存和时间必定会超
 * 经过分析，只有一个数字只会被自己和另一个数整除，最后结果才为1，即必须为平方数，故index位置为平方数时候最后结果为1
 */
class Solution0319 {
    public int bulbSwitch(int n) {
        int[] bulbArray = new int[n];
        for (int i = 1; i < n + 1; i++) {
            for (int index = i; index < n + 1; index+=i) {
                // if (index % i == 0) {
                    if (bulbArray[index - 1] == 0) {
                        bulbArray[index - 1] = 1;
                    } else {
                        bulbArray[index - 1] = 0;
                    }
                // }
            }
            System.out.println(Arrays.toString(bulbArray));
        }
        int result = 0;
        for (int index = 0; index < n; index++) {
            if (bulbArray[index] == 1) {
                result++;
            }
        }

        // int result = 0;
        // int gap=1;
        // for(int i=0;i<n;i+=gap){
        //     result++;
        //     gap+=2;
        // }

        return result;
    }

    public static void main(String[] s) throws Exception {
        Solution0319 Solution0319 = new Solution0319();
        System.out.println(Solution0319.bulbSwitch(30));
        // for(int i=0;i<999;i++){
        //     System.out.println(Solution0319.bulbSwitch(i));
        // }
    }
}