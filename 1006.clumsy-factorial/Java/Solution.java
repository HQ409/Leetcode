package Java;

import java.util.Stack;

/**
 * @see <a href="https://leetcode-cn.com/problems/clumsy-factorial/"></a>
 * 1006. 笨阶乘
 */
class Solution1006 {
    void output(Object object) {
        System.out.println(object);
    }

    public int clumsy(int N) {
        //数字栈
        Stack<Integer> numStack = new Stack();
        //操作符栈，加号为1，减号为-1，乘号为2，除号为-2
        numStack.push(N);
        Stack<Integer> operatorStack = new Stack();

        StringBuffer operateStringBuffer = new StringBuffer();
        operateStringBuffer.append(N);

        for (int i = N - 1; i > 0; i--) {
            switch ((N - i) % 4) {
                case 1:
                    operateStringBuffer.append("*").append(i);
                    operate(numStack, operatorStack, i, 2);
                    break;
                case 2:
                    operateStringBuffer.append("/").append(i);
                    operate(numStack, operatorStack, i, -2);
                    break;
                case 3:
                    operateStringBuffer.append("+").append(i);
                    operate(numStack, operatorStack, i, 1);
                    break;
                case 0:
                    operateStringBuffer.append("-").append(i);
                    operate(numStack, operatorStack, i, -1);
                    break;
            }
        }
        while (!operatorStack.isEmpty()) {
            operate(numStack, operatorStack);
        }

        operateStringBuffer.append("=").append(numStack.peek());
        output(operateStringBuffer);
        return numStack.peek();
    }

    void operate(Stack<Integer> numStack, Stack<Integer> operatorStack, int num, int operator) {
        output("numStack:" + numStack + ",operatorStack:" + operatorStack + ",num:" + num + ",operator:" + operator);
        while (!operatorStack.isEmpty() && Math.abs(operatorStack.peek()) >= Math.abs(operator)) {
            operate(numStack, operatorStack);
        }
        operatorStack.push(operator);
        numStack.push(num);
    }

    void operate(Stack<Integer> numStack, Stack<Integer> operatorStack) {

        int operator1 = numStack.pop();
        int operator2 = numStack.pop();
        switch (operatorStack.pop()) {
            case 2:
                output(operator1 + "*" + operator2);
                numStack.push(operator1 * operator2);
                break;
            case -2:
                output(operator2 + "/" + operator1);
                numStack.push(operator2 / operator1);
                break;
            case 1:
                output(operator1 + "+" + operator2);
                numStack.push(operator1 + operator2);
                break;
            case -1:
                output(operator2 + "-" + operator1);
                numStack.push(operator2 - operator1);
                break;
        }
    }

    public static void main(String[] s) throws Exception {
        Solution1006 Solution1006 = new Solution1006();
        System.out.println(Solution1006.clumsy(10));
    }
}