class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        result = []

        for i in range (len(nums)-1,1,-1):
            if (i<=0):
                break
            if i<(len(nums)-1) and snums[i] == snums[i+1]:
                continue
            mini = 0
            maxi = i-1   
            while mini < maxi:
                total = snums[i] + snums[mini] + snums[maxi]
                if total<0:
                    mini+=1
                elif total>0:
                    maxi-=1
                elif total ==0:
                    result.append([snums[mini] , snums[maxi],snums[i]])
                    mini+=1
                    maxi-=1
                    while (mini < maxi) and snums[maxi] == snums[maxi + 1]:                        
                        maxi -= 1
        return result
        
