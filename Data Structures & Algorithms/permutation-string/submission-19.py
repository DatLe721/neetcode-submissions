class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        l=0
        se = set(s1)
        for s1s in s1:
            dic[s1s] = 1+ dic.get(s1s,0)
        for i in range (len(s2)):
            if i-l+1>len(s1):
                if s2[l] in dic:
                    dic[s2[l]]+=1
                    if dic[s2[l]]>0:
                        se.add(s2[l])
                l+=1
            if s2[i] in dic:
                dic[s2[i]]-=1
                if (dic[s2[i]]==0):
                    se.remove(s2[i])  
                    if len(se)==0:
                        
                        return True                     
        
        return False