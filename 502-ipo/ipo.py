class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        proj=[]
        for i in range(len(profits)):
            proj.append([capital[i],profits[i]])
        proj.sort()

        heap=[]
        idx=0
        while k:
            while idx <len(proj) and proj[idx][0] <=w:
                heapq.heappush(heap,-proj[idx][1])
                idx +=1
            if not heap:
                break
            w-=heapq.heappop(heap)
            k-=1
        return w

        