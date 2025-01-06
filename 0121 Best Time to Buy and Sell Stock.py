class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # One pointer iteration
        # time n
        # space 1
        profit, buy = 0, float('inf')
        
        for p in prices:
            if p < buy:
                buy = p
            elif profit < p - buy:
                profit = p - buy
        
        return profit

        '''
        # Sliding window | Two pointers
        # Time: O(n)
        # Space: O(1)
        while sell < len(prices):
            if prices[sell] - prices[buy] < 0:
                buy += 1
                sell = buy + 1
            else:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
            
        return profit
        '''
