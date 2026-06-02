class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #do binary search on the rows
        low, high = 0, len(matrix) - 1

        while low <= high:
            middle = (low + high) // 2
            if matrix[middle][-1] < target:
                low = middle + 1
            elif matrix[middle][0] > target:
                high = middle - 1
            else:
                break
        
        #middle == row #
        #do binary search on one of the rows
        l, r = 0, len(matrix[middle]) - 1

        while l <= r:
            m = (l + r) //2
            if matrix[middle][m] == target:
                return True
            elif matrix[middle][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False