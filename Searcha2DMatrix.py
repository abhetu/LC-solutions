class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # I would first initialize top and bottom pointers to check where the target falls
       # after that I would check if the target is in thge middle row or not by checking if it is smaller than the left most value or bigger than the right most value
       # if it is found then just break the condition and return true
       # if not i would move the bottom pointer to up if the value is less
       # if the value is more i would move the top pointer below 
       # and then i would again binary search in the row and then check if it falls under that
       # make sure if the middle is the target, if middle > target then move left to middle + 1
       # if middle < target then move right to middle - 1
       # and then i would return true if the target exists if not return fgalse
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

            
        if not (top <= bot):
            return False

        row = (top + bot) // 2
        l,r = 0, COLS - 1
        while l<=r:
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False   
        