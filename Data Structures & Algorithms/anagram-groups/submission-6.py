class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        result = []
        for str in strs:
            dic[''.join(sorted(str))].append(str)
        return list(dic.values())