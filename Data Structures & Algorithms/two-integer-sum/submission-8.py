class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other={}
        for e,n in enumerate(nums):
            other[n] = e
        print(other)
        for i in range (len(nums)):
                remain = target-nums[i]
                if remain in nums and other[remain] !=i:
                        return [i,other[remain]]
