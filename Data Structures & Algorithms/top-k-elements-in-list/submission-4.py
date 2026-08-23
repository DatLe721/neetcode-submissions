class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n , i in count.items():
            result[i].append(n)
        end=[]
        for i in range(len(result)-1, 0 , -1):
            for n in result[i]:
                end.append(n)
                if len(end) == k:
                    return end
        