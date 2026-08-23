class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total = []
        seen = []
        for i in range(len(strs)):
            if sorted(strs[i]) not in seen:
                seen.append(sorted(strs[i]))
                total.append([strs[i]])
                print(seen)
            else:
                for e in range(len(seen)):
                    if seen[e] == sorted(strs[i]):
                        total[e].append(strs[i])
        return total