package Java;

/**
 * @see <a href="https://leetcode-cn.com/problems/iterator-for-combination/"></a>
 * 1286. 字母组合迭代器
 */
class CombinationIterator {
    int currentIndex = 0;
    String characters;
    int charactersLength;
    int combinationLength;
    long totalLength;
    int[] indexArray;
    char[] charArray;

    public CombinationIterator(String characters, int combinationLength) {
        this.characters = characters;
        this.combinationLength = combinationLength;
        charactersLength = characters.length();
        totalLength = factorial(charactersLength) / (factorial(combinationLength) * factorial(charactersLength - combinationLength));
        indexArray = new int[combinationLength];
        for (int i = 0; i < combinationLength; i++) {
            indexArray[i] = i;
        }
        charArray = characters.toCharArray();
    }

    public String next() {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < indexArray.length; i++) {
            stringBuilder.append(charArray[indexArray[i]]);
        }

        if (currentIndex  < totalLength) {
            for (int i = indexArray.length - 1; i >= 0; i--) {
                //判断当前位是否达到上限，未达到则递增直到达到上限，未达到则运算下一位,每一位的上限是 charactersLength-combinationLength+i
                if (indexArray[i] < (charactersLength - combinationLength + i)) {
                    indexArray[i] = indexArray[i] + 1;
                    //初始化以后位置
                    for (int j = i + 1; j < indexArray.length; j++) {
                        indexArray[j] = indexArray[j - 1] + 1;
                    }
                    break;
                }
            }
        }

        currentIndex++;

        return stringBuilder.toString();
    }

    public boolean hasNext() {
        return currentIndex  < totalLength;
    }

    long factorial(int number) {
        if (number <= 1) {
            return 1;
        }
        return number * factorial(number - 1);
    }


    public static void main(String[] s) throws Exception {
        CombinationIterator CombinationIterator = new CombinationIterator("aceghjlmnqsuwxy", 7);
        while(CombinationIterator.hasNext()){
            System.out.println(CombinationIterator.next());
        }

    }
}