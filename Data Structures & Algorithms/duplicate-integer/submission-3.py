class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         for i in range (len(nums)):
            target = nums[i]
            for e in range (len(nums)):
                if e!= i:
                    if target == nums[e]:
                        return True
         return False