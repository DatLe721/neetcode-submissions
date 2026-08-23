class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss,ts = {},{}
        for i in range(len(s)):
            ss[s[i]] = 1 + ss.get(s[i],0)
            ts[t[i]] = 1 + ts.get(t[i],0)
        
        if ss == ts:
            return True
        return False