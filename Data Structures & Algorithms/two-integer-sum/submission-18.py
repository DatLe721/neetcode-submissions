class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,e in enumerate(nums):
            diff = target-e
            if diff in dic:
                return [dic[diff],i]
            dic[e] = i

        
