class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointers
        # Time O(n)
        # Space O(1)

        # We start two pointers from left and right of an array
        # So that we could get maxmimum width at start
        maxAmount, left, right = 0, 0, len(height)-1
        
        while left < right:
            # Calculate current amount considering left and right pointers
            currentAmount = (right - left) * min(height[left], height[right])
            if currentAmount > maxAmount:
                maxAmount = currentAmount

            # Here we will keep greater bar pointer steady and move another
            # If left bar is greater than right, move right pointer inwards
            if height[left] > height[right]:
                right-=1
            # else if right bar is greater then move left pointer inwards
            else:
                left+=1

        return maxAmount
