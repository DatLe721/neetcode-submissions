class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        current = min(heights[left],heights[right])*(right-left)
        maxh = current
        while left < right:
            if heights[left]>=heights[right]:
                right-=1
            elif heights[left]<heights[right]:
                left+=1
            current = min(heights[left],heights[right])*(right-left)
            maxh = max(maxh,current)
        return maxh