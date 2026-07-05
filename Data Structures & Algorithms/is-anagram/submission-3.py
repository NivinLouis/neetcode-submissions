class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        CountS = {}
        CountT = {}

        if len(s) != len(t):
            return False
            exit()
        
        for i in range(len(s)):
            if s[i] not in CountS:
                CountS[s[i]]=1
            else:
                CountS[s[i]]=CountS[s[i]]+1
            if t[i] not in CountT:
                CountT[t[i]]=1
            else:
                CountT[t[i]]=CountT[t[i]]+1
        
        return CountT == CountS