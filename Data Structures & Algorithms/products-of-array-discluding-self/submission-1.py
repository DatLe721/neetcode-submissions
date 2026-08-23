class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        result = []
        for i in range (len(nums)):
            if (i ==0):
                pre.append(nums[0])
                post.append(nums[len(nums)-1])
            else:
                pre.append(nums[i]*pre[len(pre)-1])
                post.append(nums[len(nums)-i-1]*post[len(post)-1])
        print(pre)
        print(post)
        for i in range(len(nums)):
            if (i==0):
                result.append(post[len(post)-2])
            elif (i == len(nums)-1):
                result.append(pre[len(pre)-2])
            else:
                result.append(pre[i-1]*post[len(post)-2-i])
            print(result)
        return result

