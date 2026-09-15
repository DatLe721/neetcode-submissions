class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        outc = []
        q = deque()
        for i in range(len(nums)):
            if q and q[0]<i-k+1:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if q[-1]>=k-1:
                outc.append(nums[q[0]])
        return outc
            
            
