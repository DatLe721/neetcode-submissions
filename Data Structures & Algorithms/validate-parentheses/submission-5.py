class Solution:
    def isValid(self, s: str) -> bool:
        list1=[]
        for i in range(len(s)):
            if(len(list1)>0 and s[i] == ")" and list1[len(list1)-1]=="("):
                list1.pop()
            elif(len(list1)>0 and s[i] == "]" and list1[len(list1)-1]=="["):
                list1.pop()
            elif(len(list1)>0 and s[i] == "}" and list1[len(list1)-1]=="{"):
                list1.pop()
            else:
                list1.append(s[i])
        if len(list1)!=0:
            return False
        return True