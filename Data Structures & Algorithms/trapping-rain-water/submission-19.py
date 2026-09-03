class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        total = 0
        if (len(height)<3):
            return(0)

        i=l
        maxl = height[l]
        maxr= height[r]
 
        while l<r:
            if maxl<maxr:
                l+=1
                maxl = max(maxl, height[l])
                total += (maxl-height[l])  
            else:
                r-=1
                maxr = max(maxr, height[r])
                total += (maxr-height[r])
                
        return total




