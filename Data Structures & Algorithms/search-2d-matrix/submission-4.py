class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #base case:
        
        #do binary search on the rows
        rows, cols = len(matrix), len(matrix[0])
        bot, top = 0, rows-1

        while bot <= top:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                bot = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else:
                break

        if bot > top:
            return False
        #binary search
        l,r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else: 
                r = mid - 1
        return False