package Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @see <a href="https://leetcode-cn.com/problems/spiral-matrix/"></a>
 * 54. 螺旋矩阵
 */
class Solution54 {
    int currentHang = 0;
    int currentLie = 0;
    //前进方向，1：向右 2：向下 3：向左 4：向上 ，如果某个方向无法前进，则按照1，2，3，4，1的循环前进
    int direction = 1;
    int tryTimes = 0;

    //获取下一个节点，返回0代表可行并已行走，非0则为不可行，因为只有四个方向，所以超过4则为结束
    private int goNext(int[][] flagMatrix) {
        //先看正常走法是否下个节点可行
        int nextHang = currentHang;
        int nextLie = currentLie;
        switch (direction) {
            case 1:
                nextLie++;
                break;
            case 2:
                nextHang++;
                break;
            case 3:
                nextLie--;
                break;
            case 4:
                nextHang--;
                break;
        }
        if (flagMatrix[nextHang + 1][nextLie + 1] == 0) {
            //正常走法可行，则改变值然后返回
            currentHang = nextHang;
            currentLie = nextLie;
            tryTimes = 0;
            return 0;
        } else {
            //如果前方行不通，就考虑转方向
            switch (direction) {
                case 1:
                    direction = 2;
                    break;
                case 2:
                    direction = 3;
                    break;
                case 3:
                    direction = 4;
                    break;
                case 4:
                    direction = 1;
                    break;
            }
            tryTimes++;
            if(tryTimes>3){
                return -1;
            }
            return goNext(flagMatrix);
        }
    }

    public List<Integer> spiralOrder(int[][] matrix) {
        int length = matrix[0].length;
        int width = matrix.length;
        //建立长宽均比matrix大2的矩阵判断是否已访问
        int[][] flagMatrix = new int[width + 2][length + 2];
        //边界列均设置为已访问，中间列设置为未访问
        for (int i = 0; i < length + 2; i++) {
            flagMatrix[0][i] = 1;
            flagMatrix[width + 1][i] = 1;
        }
        for (int i = 0; i < width + 2; i++) {
            flagMatrix[i][0] = 1;
            flagMatrix[i][length + 1] = 1;
        }

        System.out.println(Arrays.deepToString(flagMatrix));

        List<Integer> resultList = new ArrayList<>();

        resultList.add(matrix[0][0]);
        flagMatrix[1][1] = 1;

        while (goNext(flagMatrix) == 0) {
            //先将值添加到list里
            resultList.add(matrix[currentHang][currentLie]);
            // System.out.println(resultList);
            //将对应位置的访问矩阵设置为1
            flagMatrix[currentHang + 1][currentLie + 1] = 1;
            // System.out.println(Arrays.deepToString(flagMatrix));
        }

        return resultList;
    }

    public static void main(String[] s) throws Exception {
        int[][] matrix = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
        System.out.println(new Solution54().spiralOrder(matrix));
    }
}