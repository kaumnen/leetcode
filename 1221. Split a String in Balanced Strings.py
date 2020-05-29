class Solution:
    def balancedStringSplit(self, s: str) -> int:
        temp = 0
        result = 0
        for letter in s:
            
            if letter == 'R':
                temp += 1
                
            else:
                temp -= 1
                
            if temp == 0:
                result += 1
                
        return result
