class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters=[]
        sorted_str = ''.join(sorted(s, key=str.lower))
        sorted_str2 = ''.join(sorted(t, key=str.lower))
        if sorted_str == sorted_str2:
            return True
        return False