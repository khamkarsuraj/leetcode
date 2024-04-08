class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Using Map
        // Time: O(n)
        // Space: O(n)
        Map<Integer, Integer> d = new HashMap<Integer, Integer>();
        int[] ret = new int[2];

        for (int i=0; i<nums.length; i++) {
            int rem = target - nums[i];

            if (d.get(rem) != null) {
                ret[0] = i;
                ret[1] = d.get(rem);
                return ret;
            }

            d.put(nums[i], i);
        }

        return ret;

    }
}
