class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        window = []
        se = set()
        res = 0
        for r in range (len(s)):
            if s[r] in se:
                while s[l]!= s[r]:
                    se.remove(s[l])
                    l+=1
                se.remove(s[l])
                l+=1
            window.append(s[r])
            se.add(s[r])
            res = max(res,len(se))
        return res
            
