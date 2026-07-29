class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        # for i in range(n):
        #     for j in range(i, n):
        #         w = j - i
        #         h = min(heights[i], heights[j])
        #         area = w*h
        #         max_area = max(max_area, area)

        r,l = n -1, 0 
        max_area = 0
        while l < r:

            w = r - l
            h = min(heights[l], heights[r])
            area = w * h
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area