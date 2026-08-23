class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            dic[num] = 0
        
        for num in nums:
            dic[num]+=1
            if dic[num]>1:
                return True
        return False
            
        