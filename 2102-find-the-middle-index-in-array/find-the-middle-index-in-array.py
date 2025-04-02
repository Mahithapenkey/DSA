class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n= len(nums)
        left = [0]*n
        right=[0]*n
        for i in range(1,n):
            left[i]=left[i-1]+nums[i-1]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] + nums[i+1]
        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1
        
        