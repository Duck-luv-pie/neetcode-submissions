class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first do bs to find which row
        l,r = 0, len(matrix) - 1

        while l <= r:
            row = (l+r) // 2

            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            elif target < matrix[row][0]:
                r = row - 1
            else:
                l = row + 1
            


        #then do bs on the row
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l+r) // 2

            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False