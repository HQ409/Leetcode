package Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @see <a href="https://leetcode-cn.com/problems/subsets-ii/"></a>
 * 90. 子集 II
 */
class Solution90 {
    int runTimes=0;
    // 我的笨答案

    // public List<List<Integer>> subsetsWithDup(int[] nums) {
    //     List<List<Integer>> resultList = new ArrayList<>();
    //     resultList.add(new ArrayList<>());
    //     List<Integer> numsList = Arrays.stream(nums).sorted().boxed().collect(Collectors.toList());
    //     resultList.add(numsList);
    //     handleSubArray(resultList, numsList);
    //     return resultList;
    // }
    //
    // void handleSubArray(List<List<Integer>> resultList, List<Integer> nums) {
    //     for (int i = 0; i < nums.size(); i++) {
    //
    //         List<Integer> subNums = new ArrayList<>(nums);
    //         subNums.remove(i);
    //         if (!resultList.contains(subNums)) {
    //             resultList.add(subNums);
    //             handleSubArray(resultList, subNums);
    //         }
    //     }
    // }

    //别人的NB答案
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> ans=new ArrayList<>();
        Arrays.sort(nums);
        getAns(nums,0,new ArrayList<>(),ans);
        return ans;
    }

    private void getAns(int[] nums,int start, ArrayList<Integer> tmp, List<List<Integer>> ans){
        System.out.println(Arrays.toString(nums)+"====="+start+"====="+tmp);
        ans.add(new ArrayList<>(tmp));
        for(int i=start;i<nums.length;i++){
            if(i>start&&nums[i]==nums[i-1])continue;
            tmp.add(nums[i]);
            getAns(nums,i+1,tmp,ans);
            tmp.remove(tmp.size()-1);
        }
    }


    public static void main(String[] s) throws Exception {
        Solution90 Solution90 = new Solution90();
        Solution90.subsetsWithDup(new int[]{1,2,2});

        // Solution90.subsetsWithDup(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 10, 0});
    }
}