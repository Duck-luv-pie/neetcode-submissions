class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        f,l = 0, len(matrix) - 1
        
        while f <= l:
            row = (f+l)//2
            if matrix[row][-1] < target:
                f = row + 1
            elif matrix[row][0] > target:
                l = row - 1
            else:
                break;
        
        l, r = 0, len(matrix[row]) -1

        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False