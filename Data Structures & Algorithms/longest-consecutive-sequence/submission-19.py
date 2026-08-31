class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        current = 1
        longest = 0
        num = 0
    
        for x in num_set:
            if (x-1) not in num_set:
                num = x
                current= 1
                while num+1 in num_set:
                    current+=1
                    num+=1
                longest = max(longest,current)
        return longest