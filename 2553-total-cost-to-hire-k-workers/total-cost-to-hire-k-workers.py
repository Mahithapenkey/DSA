class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        min_heap=[]
        left=0
        right = len(costs) -1
        total_cost=0

        for i in range(candidates):
            if left<=right:
                heapq.heappush(min_heap,(costs[left],left))
                left += 1
            if left <= right:
                heapq.heappush(min_heap,(costs[right],right))
                right-=1
       
        while k>0 and min_heap:
            cost,idx=heapq.heappop(min_heap)
            total_cost += cost
            k-=1
            if left <= right:
                if idx<left:
                    heapq.heappush(min_heap,(costs[left],left))
                    left+=1
                elif idx>right:
                    heapq.heappush(min_heap,(costs[right],right))
                    right-=1
        return total_cost
        