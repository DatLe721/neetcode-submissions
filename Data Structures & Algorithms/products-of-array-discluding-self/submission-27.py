class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        dic = {}
        dic_right={}
        result=[0]*len(nums)
        for i in range (1,len(nums)):
            if i == 1:
                dic[i] = nums[0]
            else:
                dic[i] = dic[i-1]*nums[i-1]

        for i in range (len(nums)-2,-1,-1):
            if i == (len(nums)-2):
                dic_right[(len(nums)-2)] = nums[(len(nums)-1)]
            else:
                dic_right[i] = dic_right[i+1]*nums[i+1]

        for i in range (0,len(nums)):
            if i ==0:
                result[i] = dic_right[i]
            elif i==len(nums)-1:
                result[i]= dic[i]
            else:
                result[i] = dic[i]*dic_right[i]

        return result

