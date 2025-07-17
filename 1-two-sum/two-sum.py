class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict={}
        for i,num in enumerate(nums):
            comp=target-nums[i]
            if comp in num_dict:
                return [num_dict[comp],i]
            num_dict[num]=i
        return []
            
        
        
        