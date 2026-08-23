class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list = [0]*26
        for i in range (len(s)):
            list[ord(s[i])-ord('a')] +=1
            list[ord(t[i])-ord('a')] -=1
        if list!= [0]*26:
            return False
        return True