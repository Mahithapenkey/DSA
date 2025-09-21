class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if not nums:
            return 0
        k=0
        for i in range(n):
            if nums[i]!=nums[k]:
                k+=1
                nums[k]=nums[i]
        return k+1
        