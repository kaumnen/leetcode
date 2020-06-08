class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        temp = 0
        i = 0
        while temp < n:
            temp = 2 ** i
            if temp == n:
                return True
            i += 1
        return False
