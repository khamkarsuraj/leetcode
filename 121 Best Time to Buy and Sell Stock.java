class Solution {
    public int maxProfit(int[] prices) {
        // One Pointer | Iterative Method
        // Time: O(n)
        // Space: O(1)
        int profit = 0;
        int buy = Integer.MAX_VALUE;

        for(int i=0; i<prices.length; i++) {
            if (prices[i] < buy) {
                buy = prices[i];
            } else if (profit < prices[i] - buy) {
                profit = prices[i] - buy;
            }
        }

        return profit;
    }
}
