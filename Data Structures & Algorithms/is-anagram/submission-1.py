class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqOfS = {}
        freqOfT = {}
        if len(s) != len(t): return False

        for i in s:
            if i in freqOfS:
                freqOfS[i] += 1
            else:
                freqOfS[i] = 1
        
        for i in t:
            if i in freqOfT:
                freqOfT[i] += 1
            else:
                freqOfT[i] = 1

        return freqOfT==freqOfS

        
        