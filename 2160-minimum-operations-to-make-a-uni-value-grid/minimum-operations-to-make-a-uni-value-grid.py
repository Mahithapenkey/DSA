class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums=[]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]%x != grid[0][0] % x:
                    return -1
                nums.append(grid[row][col])
        nums.sort()
        mid = nums[len(nums)//2]
        count=0
        for num in nums:
            count+= abs(num - mid)//x
        return count




        