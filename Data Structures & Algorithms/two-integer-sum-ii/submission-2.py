class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        stat = True
        bee = 0
        end = len(numbers)-1
        while(numbers[bee]+numbers[end]!=target):
            if numbers[bee]+numbers[end]>target:
                end-=1
            else:
                bee+=1
        return [bee+1,end+1]