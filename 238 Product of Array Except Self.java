class Solution {
    public int[] productExceptSelf(int[] nums) {
        // Using Prefix Suffix product
        // Time: O(n)
        // Space: O(n)
        int pro = 1;
        int[] ans = new int[nums.length];
        // First go through input array
        // calculate prefix product of each element
        for(int i=0; i<nums.length; i++) {
            ans[i] = pro;
            pro = pro * nums[i];
        }

        // Then, go through output array once again
        // Calculate suffix product considering input array
        pro = 1;
        for(int i=nums.length-1; i>=0; i--) {
            ans[i] = ans[i] * pro;
            pro = pro * nums[i];
        }

        return ans;

        /*
        // Using Division Operator
        // Time: O(n^2)
        // Space: O(1)
        int total_product = 1;
        for (int i=0; i<nums.length; i++) {
            total_product = total_product * nums[i];
        }

        int[] answer = new int[nums.length];
        for (int i=0; i<nums.length; i++) {
            if (nums[i] != 0) answer[i] = total_product / nums[i];
            else {
                int prod = 1;
                for (int j=0; j<nums.length; j++) {
                    if (i != j) {
                        prod = prod * nums[j];
                    }
                }
                answer[i] = prod;
            }
        }

        return answer;
        */

        /*
        // Brute Force Method
        // Time: O(n^2) TLE
        // Space: O(1)
        int[] answer = new int[nums.length]; 
        for (int i=0; i<nums.length; i++) {
            int prod = 1;
            for (int j=0; j<nums.length; j++) {
                if (i != j) {
                    prod = prod * nums[j];
                }
            }
            answer[i] = prod;
        }

        return answer;
        */
    }
}
