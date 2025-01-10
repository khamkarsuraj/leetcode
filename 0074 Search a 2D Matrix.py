class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # time logmn
        # space 1
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
    
        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // n][mid % n]  # Convert 1D index to 2D row and column
    
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

        # # time logm + logn
        # # space 1
        # m = len(matrix)
        # n = len(matrix[0])
        # l, r = 0, m-1
        # while l <= r:
        #     m = (l+r)//2
        #     if target >= matrix[m][0] and target <= matrix[m][n-1]:
        #         # binary search 
        #         l, r, row = 0, n-1, m
        #         while l <= r:
        #             m = (l+r)//2
        #             if target == matrix[row][m]:
        #                 return True
        #             elif target < matrix[row][m]:
        #                 r = m - 1
        #             else:
        #                 l = m + 1
        #         break

        #     elif target < matrix[m][0]:
        #         r = m - 1
        #     else:
        #         l = m + 1
    
        # return False

        # # loops
        # # time mn
        # # space 1
        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     if target <= matrix[i][n-1]:
        #         for j in range(n):
        #             if target == matrix[i][j]:
        #                 return True

        # return False

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
