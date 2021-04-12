package Java;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @see <a href="https://leetcode-cn.com/problems/volume-of-histogram-lcci/"></a>
 * 面试题 17.21. 直方图的水量
 * 思路：获取每个高度最左侧和最右侧的坐标，去掉这个高度墙占用的面积，即为这个高度可以蓄水的面积
 * 注意有些高度段是同模的，针对同模的只需要一次遍历
 */
class Solution2013 {
    void output(Object object) {
        System.out.println(object);
    }

    public int trap(int[] height) {
        int leftIndex = 0;
        int rightIndex = height.length - 1;
        int answer = 0;
        int calLevel = 0;

        int sum = 0;
        int maxHeight = 0;
        int secondMaxHeight = 0;

        while (leftIndex < rightIndex) {
            int leftHeight = height[leftIndex];
            int rightHeight = height[rightIndex];
            while (leftHeight == 0) {
                leftIndex++;
                leftHeight = height[leftIndex];
            }
            while (rightHeight == 0) {
                rightIndex--;
                rightHeight = height[rightIndex];
            }

            if (leftIndex == rightIndex) {
                return answer - sum + (maxHeight - secondMaxHeight);
            }

            sum += leftHeight;
            output("sum += leftHeight:"+leftHeight);
            sum += rightHeight;
            output("sum += leftHeight:"+rightHeight);

            if (leftHeight >= rightHeight) {
                if (leftHeight > maxHeight) {
                    secondMaxHeight = Math.max(maxHeight, rightHeight);
                    maxHeight = leftHeight;
                }
                int newArea = (rightHeight - calLevel) * (rightIndex - leftIndex + 1);

                output("leftIndex:" + leftIndex + ",rightIndex:" + rightIndex + ",leftHeight:" + leftHeight + ",rightHeight:" + rightHeight + ",calLevel:" + calLevel + ",newArea:" + newArea);

                answer += newArea;
                calLevel = rightHeight;
                while (height[rightIndex] <= rightHeight && leftIndex < rightIndex) {
                    rightIndex--;
                    if (height[rightIndex] > secondMaxHeight && height[rightIndex] < maxHeight) {
                        secondMaxHeight = height[rightHeight];
                    }
                    if(leftIndex<rightIndex){
                        sum += height[rightIndex];
                        output("sum += height[rightIndex]:"+height[rightIndex]);
                    }

                }
            } else {
                if (rightHeight > maxHeight) {
                    secondMaxHeight = Math.max(maxHeight, leftHeight);
                    maxHeight = rightHeight;
                }
                int newArea = (leftHeight - calLevel) * (rightIndex - leftIndex + 1);

                output("leftIndex:" + leftIndex + ",rightIndex:" + rightIndex + ",leftHeight:" + leftHeight + ",rightHeight:" + rightHeight + ",calLevel:" + calLevel + ",newArea:" + newArea);

                answer += newArea;
                calLevel = leftHeight;
                while (height[leftIndex] <= leftHeight && leftIndex < rightIndex) {
                    leftIndex++;
                    if (height[leftIndex] > secondMaxHeight && height[leftIndex] < maxHeight) {
                        secondMaxHeight = height[leftIndex];
                    }
                    if(leftIndex<rightIndex){
                        sum += height[leftIndex];
                        output("sum += height[leftIndex]:"+height[leftIndex]);
                    }
                }
            }

        }

        if (leftIndex == rightIndex) {
            return answer - sum + (maxHeight - secondMaxHeight);
        } else {
            return answer - sum;
        }

    }


    public int stupidTrap(int[] height) {
        List<Integer> levelList = Arrays.stream(height).boxed().distinct().sorted().collect(Collectors.toList());
        //比如如果高度为0，1，3，10，则level为2的结果同level3的结果
        if (levelList.size() < 2) {
            return 0;
        }
        int answer = 0;
        for (int index = 0; index < levelList.size(); index++) {
            int level = levelList.get(index);
            if (level == 0) {
                continue;
            }

            int leftPoint = -1;
            int rightPoint = -1;
            int holdNum = -2;
            for (int i = 0; i < height.length; i++) {
                if (height[i] >= level && leftPoint == -1) {
                    leftPoint = i;
                }
                if (height[i] >= level && i > rightPoint) {
                    rightPoint = i;
                }
                if (leftPoint != -1 && rightPoint != -1) {
                    if (height[i] >= level) {
                        holdNum++;
                    }
                }
            }
            if (leftPoint == rightPoint) {
                continue;
            }

            int actuallyLevel = 0;
            if (index >= 1) {
                actuallyLevel = level - levelList.get(index - 1);
            } else {
                actuallyLevel = level;
            }

            int waterSize = rightPoint - leftPoint - 1 - holdNum;

            output("level:" + level + ",leftPoint:" + leftPoint + ",rightPoint:" + rightPoint + ",holdNum:" + holdNum + ",actuallyLevel:" + actuallyLevel + ",waterSize:" + waterSize);

            answer += waterSize * actuallyLevel;
        }

        return answer;
    }

    public static void main(String[] s) throws Exception {
        Solution2013 Solution2013 = new Solution2013();
        System.out.println(Solution2013.trap(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}));
        System.out.println(Solution2013.stupidTrap(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}));
        // System.out.println(Solution2013.trap(new int[]{}));
        // System.out.println(Solution2013.trap(new int[]{4, 2, 0, 3, 2, 5}));
        // System.out.println(Solution2013.stupidTrap(new int[]{4, 2, 0, 3, 2, 5}));
        // System.out.println(Solution2013.trap(new int[]{2, 0, 2}));
        // System.out.println(Solution2013.trap(new int[]{0, 2, 0}));
        // System.out.println(Solution2013.trap(new int[]{6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3}));

        // BufferedReader br = null;
        // try {
        //     InputStreamReader isr = new InputStreamReader(new FileInputStream("/Users/walsli/Downloads/testcase.txt"), "utf-8");
        //     br = new BufferedReader(isr);
        //     String text = br.readLine();
        //
        //     Object[] oarray = Arrays.stream(text.split(",")).map(Integer::parseInt).toArray();
        //     int[] array = new int[oarray.length];
        //     for (int i = 0; i < array.length; i++) {
        //         array[i] = (int) oarray[i];
        //     }
        //     System.out.println(Solution2013.trap(array));
        //     System.out.println(Solution2013.stupidTrap(array));
        //     br.close();
        // } catch (Exception e) {
        //     e.printStackTrace();
        // } finally {
        //     if (br != null) {
        //         try {
        //             br.close();
        //         } catch (Exception e) {
        //             e.printStackTrace();
        //         }
        //     }
        // }


    }
}