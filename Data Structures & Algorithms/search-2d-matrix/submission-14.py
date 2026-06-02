class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b,t = 0, len(matrix)-1
        
        while b <= t:
            middle = (t+b)//2
            if matrix[middle][0] > target:
                t = middle - 1
            elif matrix[middle][-1] < target:
                b = middle + 1
            else:
                break
        
            


        l, r = 0, len(matrix[0])-1

        while l <= r:
            mid = (l+r)//2
            if matrix[middle][mid] == target:
                return True
            elif matrix[middle][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False