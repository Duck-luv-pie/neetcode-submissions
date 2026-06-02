class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #bs on rows
        first, last = 0, len(matrix) - 1

        while first <= last:
            row = (first + last)//2
            #case where we find it
            if matrix[row][-1] >= target and matrix[row][0] <= target: 
                break
            elif matrix[row][0] > target:
                last = row - 1
            else:
                first = row + 1

        
        #now we should have the row


        print(row)
        #bs on the row
        l,r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l+r)//2
            #in the case we find it
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
