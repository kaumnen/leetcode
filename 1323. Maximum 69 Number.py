class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        
        if num.count('6') == 0:
            return num
        
        else:
            temp = [x for x in num]
            temp[temp.index('6')] = '9'
            
            return ''.join(temp)
