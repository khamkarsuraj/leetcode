class Solution {
    public int maxSubArray(int[] nums) {
        // Kadane's Algorithm
        // Time: O(n)
        // Space: O(1)
        int sum = 0;
        int maximum = nums[0];

        for (int i=0; i<nums.length; i++) {
            sum = sum + nums[i];
            if (maximum < sum) maximum = sum;
            if (sum < 0) sum = 0;
        }
        
        return maximum;
    }
}
