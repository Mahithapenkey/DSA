class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=defaultdict(int)
        res=0
        for ch in s:
            if ch in d:
                res+=2
                del d[ch]
            else:
                d[ch]+=1
        return res+1 if len(d)>0 else res