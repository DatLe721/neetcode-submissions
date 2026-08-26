class Solution:

    def encode(self, strs: List[str]) -> str:
        stro = ""
        for stri in strs:
            stro += str(len (stri))
            stro += " "
            stro += stri
        return stro
    def decode(self, s: str) -> List[str]:
        result = []
        leng = 0
        index = ''
        while(leng is not len(s)):
            if (s[leng] is not " "):
                index +=s[leng]
                leng +=1
            else:
                leng+=1
                b = leng+1
                e = b-1 + int(index)
                result.append(s[leng:e])
                leng+=int(index)
                index = ''
            if (leng>=len(s)):
                break
        return result


        