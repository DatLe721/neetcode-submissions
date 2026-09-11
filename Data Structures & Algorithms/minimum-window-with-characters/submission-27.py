class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        res = ""
        count = {}
        total = len(t)
        maxf = float('inf')
        for i in range(len(t)):
            count[t[i]] = 1+ count.get(t[i],0)
        for i in range (len(s)):            
            if s[i] in count:
                if count[s[i]]>0:
                    total-=1
                count[s[i]] -=1
            while total ==0:
                if maxf>= (i-l+1):
                    maxf = (i-l+1)
                    res = s[l:i+1]
                if s[l] in count:
                    count[s[l]]+=1
                    if count[s[l]]>0:
                        total+=1                    
                l+=1
        return res


        