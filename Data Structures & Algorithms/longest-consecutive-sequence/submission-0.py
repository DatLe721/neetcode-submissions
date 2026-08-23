class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numss= set(nums)
        longest = 0
        current = 0
        for n in numss:
            if(n-1) not in numss:
                current+=1
                print(1)
                while (n+current) in numss:
                    current+=1
            longest = max(current,longest)
            current=0
        return longest