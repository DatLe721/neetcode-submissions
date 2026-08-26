class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        lists = [[] for _ in range(len(nums) + 1)]
        result = []
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for key, val in dic.items():
            lists[val].append(key)
        for i in range(len(lists) - 1, 0, -1):
            for num in lists[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result