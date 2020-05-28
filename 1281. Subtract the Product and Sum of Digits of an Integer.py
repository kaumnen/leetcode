class Solution:
    def subtractProductAndSum(self, n: int) -> int:
    
        def sumRec(n, s = 0, p = 1):
            
            if n > 0:
                s += n % 10
                p *= n % 10
                return sumRec(n // 10, s, p)
            
            else:
                
                return s, p
            
        s,p = sumRec(n)
        
        return p - s
