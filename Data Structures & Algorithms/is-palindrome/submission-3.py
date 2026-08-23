class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha=[chr(i) for i in range(97, 123)]
        alpha+=[chr(i) for i in range(48, 57)]
        string = ''
        for i in range (len(s)):
            if s[i].lower() in alpha:
                string+=s[i].lower()
        print(string)
        if (string ==''):
            return True
        for e in range(int(len(s)/2)):
            if (string[e]!=string[(len(string)-1)-e]):
                return False
        return True