class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)     # Number of rows
        n = len(matrix[0])  # Number of columns
        
        left, right = 0, (m * n) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Map 1D index to 2D coordinates
            row = mid // n
            col = mid % n
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False