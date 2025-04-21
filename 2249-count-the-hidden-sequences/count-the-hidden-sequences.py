class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mn=0
        mx=0
        total=0
        for diff in differences:
            total += diff
            mn=min(mn,total)
            mx=max(mx,total)

        return max(0,upper-mx+mn-lower+1)