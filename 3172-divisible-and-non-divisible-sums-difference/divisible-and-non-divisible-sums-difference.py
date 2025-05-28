class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div_lst=[]
        nondiv_lst=[]
        for i in range(1,n+1):
            if i%m==0:
                div_lst.append(i)
            else:
                nondiv_lst.append(i)
        result= sum(nondiv_lst)-sum(div_lst)
        return result
            


                
            
            
        