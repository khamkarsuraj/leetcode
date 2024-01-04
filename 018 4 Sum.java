class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> quad = new ArrayList<>();
        int n = nums.length;
        
        if (nums == null || nums.length < 4) {
            return quad;
        }
    
        Arrays.sort(nums);

        for (int i=0; i<n-3; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }

            for (int j=i+1; j<n-2; j++) {
                if (j != i+1 && nums[j] == nums[j-1]) {
                    continue;
                }

                int k = j+1;
                int l = n-1;

                while (k < l) {
                    long sum = Long.valueOf(nums[i])+Long.valueOf(nums[j])+Long.valueOf(nums[k])+Long.valueOf(nums[l]);
                    if (sum < target) {
                        k++;
                    } else if (sum > target) {
                        l--;
                    } else {
                        //add into quad array as sum = target
                        quad.add(Arrays.asList(nums[i], nums[j], nums[k], nums[l]));
                        k++;
                        l--;

                        while (k < l && nums[k] == nums[k-1]) {
                            k++;
                        }
                        while (k < l && nums[l] == nums[l+1]) {
                            l--;
                        }
                    }
                }
            }
        }
        return quad;
    }
}
