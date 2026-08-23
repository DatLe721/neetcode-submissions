class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for n in nums:
            count[n]=0
        for n in nums:
            count[n]= count[n]+1
        for i in range(k):
            biggest = next(iter(count))
            for c in count:
                if count[biggest]<count[c]:
                    biggest = c
            count.pop(biggest)
            result.append(biggest)

        return result