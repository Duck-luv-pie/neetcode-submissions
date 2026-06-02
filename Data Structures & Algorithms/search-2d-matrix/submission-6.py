class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #bs on rows
        f,l = 0, len(matrix) -1
        while f <= l:
            row = (f+l) //2
            if matrix[row][0] > target:
                l = row -1
            elif matrix[row][-1] < target:
                f = row + 1
            else:
                break;
        
        #bs on row
        i, r = 0, len(matrix[row])-1
        while i <= r:
            mid = (i + r) //2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                i = mid + 1
            else:
                r = mid -1
        return False
