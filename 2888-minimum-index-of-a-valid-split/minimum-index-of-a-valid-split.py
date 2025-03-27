class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c1=collections.Counter()
        c2=collections.Counter(nums)
        for i,num in enumerate(nums):

            c1[num] +=1
            c2[num] -=1
            if c1[num]*2 >i+1 and c2[num] *2>len(nums) - i-1:
                return i
        return -1

        