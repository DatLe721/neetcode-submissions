class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
       
        for num in nums:
            dic[num] =0
        for num in nums:
            dic[num]+=1
        new_dic = dict(sorted(dic.items(),key=lambda item: item[1], reverse=True))
        print(list(new_dic.values(),))
        return list(new_dic.keys())[:k]