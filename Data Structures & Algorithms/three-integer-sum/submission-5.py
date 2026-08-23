class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newList = sorted(nums)
        total = []
        print(newList)
        for i ,a in enumerate (newList):
            if (i>0 and newList[i]==newList[i-1]):
                continue
            l,r=i+1,len(newList)-1
            while l<r:
                target = a+newList[l]+newList[r]
                print(target)
                if target < 0:
                    l+=1
                elif target>0:
                    r-=1
                else:
                    total.append([a,newList[l],newList[r]])
                    L = l+1
                    r-=1
                    while(newList[l]==newList[L]and L<r):
                        L+=1
                    l=L
        return total