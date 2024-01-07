class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Insertion sort
        // Time: O(n^2)
        // Space: O(1)

        int i = 0;

        while(i < nums.length) {
            int j = i - 1;

            while (j >= 0 && nums[j] > nums[i]) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                j--;
                i--;
            }

            if (j>=0 && nums[j]==nums[j+1])
                return true;

            i++;
        }

        return false;

        /*
        Set<Integer> s = new HashSet<Integer>();

        for (int i=0; i<nums.length; i++) {
            if (s.contains(nums[i])) {
                return true;
            }
            s.add(nums[i]);
        }
        return false;
        */
    }
}
