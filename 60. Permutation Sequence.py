import itertools
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        temp = list(itertools.permutations(range(1, n + 1)))
        temp = sorted(temp)
        return ''.join(map(str, temp[k - 1]))
