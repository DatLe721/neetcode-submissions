class Solution:
    def isValid(self, s: str) -> bool:
        stor = []
        if len(s)%2==1:
            return False
        for i in range(len(s)):
            if s[i]=='[' or s[i]=='(' or s[i]=='{':
                stor.append(s[i])
            elif stor:
                if s[i]==']' and stor[-1] == '[':
                    stor.pop()
                elif s[i]==')' and stor[-1] == '(':
                    stor.pop()
                elif s[i]=='}' and stor[-1] == '{':
                    stor.pop()
                else:
                    return False
            else:
                return False
        return len(stor)==0