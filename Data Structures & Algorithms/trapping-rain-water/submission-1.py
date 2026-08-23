class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = [0]*len(height)
        maxr = [0]*len(height)
        total = 0
        for i in range(len(height)):
            if(i == 0):
                maxl[0] = 0
                maxr[len(height)-1] = 0
            else:
                maxl[i] = max(maxl[i-1],height[i-1])
                maxr[len(height)-1-i] = max(maxr[len(height)-i],height[len(height)-i])
        for e in range(len(height)):
            current = min(maxl[e],maxr[e])-height[e]
            if(current >0):
                total+=current
        return total
            

            