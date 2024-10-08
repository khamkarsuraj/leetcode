class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Binary Search
        Time: O(m + log(n))
        Space: O(1)
        '''
        row, col = 0, len(matrix[0])

        left, right = matrix[0][0], matrix[0][col-1]

        #Find row in which target may exist
        #O(m)
        while (target > right and len(matrix) > row+1):
            row += 1
            left = matrix[row][0]
            right = matrix[row][col - 1]

        #Use binary search to check if target exists or not
        #As we found possible row, dealing with column only
        #O(log(n))
        left, right = 0, col - 1

        while (left <= right):
            mid = (left + right) // 2

            if (target == matrix[row][mid]):
                return True

            if (target > matrix[row][mid]):
                left = mid + 1
            else:
                right = mid - 1

        return False
