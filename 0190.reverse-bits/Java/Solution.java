package Java;

/**
 * @see <a href="https://leetcode-cn.com/problems/reverse-bits/"></a>
 * 190. 颠倒二进制位
 */
class Solution190 {
    public int reverseBits(int i) {
        i = (i & 0x55555555) << 1 | (i >>> 1) & 0x55555555;
        i = (i & 0x33333333) << 2 | (i >>> 2) & 0x33333333;
        i = (i & 0x0f0f0f0f) << 4 | (i >>> 4) & 0x0f0f0f0f;
        i = (i << 24) | ((i & 0xff00) << 8) |
                ((i >>> 8) & 0xff00) | (i >>> 24);
        return i;
    }

    public static void main(String[] s) throws Exception {
        Solution190 Solution190=new Solution190();
        System.out.println(Solution190.reverseBits(43261596));
    }
}