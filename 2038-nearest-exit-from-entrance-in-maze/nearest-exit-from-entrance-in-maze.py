class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue=deque([(entrance[0],entrance[1],0)])
        nr = len(maze)
        nc=len(maze[0])
        maze[entrance[0]][entrance[1]]='+'
        
        while queue:
            row,col,steps = queue.popleft()
            neighbours=[(row-1,col),(row,col+1),(row,col-1),(row+1,col)]
            for i,j in neighbours:
                if i>=0 and i<nr and j>=0 and j<nc and maze[i][j]=='.':
                    if i==0 or i==nr-1 or j==0 or j==nc-1:
                        return steps+1
                    queue.append([i,j,steps+1])
                    maze[i][j]='+'
        return -1
        