class Solution:
    def insert(self, intervals, newInterval):
        # Time Complexity: O(n) | Space Complexity: O(n)
        start, end = newInterval[0], newInterval[1]
        
        left, right = [], []
        
        for curr_interval in intervals:
            
            if curr_interval[1] < start:
                # current interval is on the left-hand side of newInterval
                left += [curr_interval]
                
            elif curr_interval[0] > end:
                # current interval is on the right-hand side of newInterval
                right += [curr_interval]
                
            else:
                # current interval has overlap with newInterval
                # merge and update boundary
                start = min(start, curr_interval[0])
                end = max(end, curr_interval[1])
                
        return left + [[start,end]] + right    

