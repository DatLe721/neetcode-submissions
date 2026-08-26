class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str=""
        for s in strs:
            encode_str+=str(len(s))
            encode_str+=str(":")
            encode_str+=str(s)
        print(encode_str)
        return encode_str
    def decode(self, s: str) -> List[str]:
        leng = 0
        result = []
        
        while leng<(len(s)-1):
            colon = leng
            print(colon)
            while s[colon] !=':':
                colon+=1
            num = int(s[leng:colon])
            print(leng,colon)
            start = colon+1
            end = start+num
            result.append(s[start:end])
            leng = end
        return result
