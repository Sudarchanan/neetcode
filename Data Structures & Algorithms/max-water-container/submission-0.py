class Solution:
    def maxArea(self, heights: List[int]) -> int:

        leng = len(heights)-1

        l = 0
        r = leng
        maxarea = 0

        while l < r:

            area = (r - l) * min(heights[l], heights[r])

            maxarea = max(maxarea, area)

            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1

        return maxarea
        
        