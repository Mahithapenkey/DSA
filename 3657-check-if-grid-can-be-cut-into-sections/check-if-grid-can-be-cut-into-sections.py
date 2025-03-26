class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_int=[]
        y_int =[]
        for sx,sy,ex,ey in rectangles:
            x_int.append([sx,ex])
            y_int.append([sy,ey])
        x_int.sort()
        y_int.sort()
        
        xres=[]
        for ele in x_int:
            if not xres:
                xres.append(ele)
            elif xres[-1][1]<=ele[0]:
                xres.append(ele)
            else:
                xres[-1][1] = max(ele[1],xres[-1][1])
        if len(xres) >2:
            return True
        yres = []
        for ele in y_int:
            if not yres:
                yres.append(ele)
            elif yres[-1][1]<=ele[0]:
                yres.append(ele)
            else:
                yres[-1][1]=max(ele[1],yres[-1][1])
        if len(yres) >2:
            return True
        return False


          
