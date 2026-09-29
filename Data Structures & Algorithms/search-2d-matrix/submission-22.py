class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) //2

            if target < matrix[mid][0]:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                break
    

        row = mid

        l, r = 0, len(matrix[0]) - 1
        
        while l <= r:
            mid = (l + r) //2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
            