class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find row w/ binary search
        #look at first in top, and last in bottom len
        if target < matrix[0][0]:
            return False
        elif matrix[-1][-1] < target:
            return False
        

        top, bottom = 0, len(matrix)-1
        n = len(matrix[0])-1
        while top <= bottom:
            middle = top + (bottom-top)//2
            if matrix[middle][n] == target: # check the last one in row
                return True
            elif target < matrix[middle][n]:
                bottom = middle - 1
            elif target > matrix[middle][n]:
                top = middle + 1
        
        

        #find col in the row with binary search
        left, right = 0, n
        while left <= right:
            middle = left + (right - left)//2
            if matrix[top][middle] == target:
                return True
            elif target < matrix[top][middle]:
                right = middle - 1
            elif target > matrix[top][middle]:
                left = middle + 1
        
        return False