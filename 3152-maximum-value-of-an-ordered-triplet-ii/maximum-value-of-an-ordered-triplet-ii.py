class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        left_max =[0]*n
        right_max = [0]*n
        left_max[0] = nums[0]
        right_max[-1] = nums[-1]

        for i in range(1,n):
            left_max[i]=max(left_max[i-1],nums[i])
        for k in range(n-2,-1,-1):
            right_max[k] = max(right_max[k+1],nums[k])
        res=0
        for j in range(1,n-1):
            ele=(left_max[j-1]-nums[j])*right_max[j+1]
            res=max(res,ele)
        return res