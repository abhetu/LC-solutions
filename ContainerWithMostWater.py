class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])  # Correct width calculation
            res = max(res, area)

            if heights[l] < heights[r]:  
                l += 1  # Move left pointer if left height is smaller
            elif heights[l] > heights[r]:  
                r -= 1  # Move right pointer if right height is smaller
            else:  
                l += 1  # Move both if they are equal
                r -= 1

        return res
