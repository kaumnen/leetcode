class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(x) for x in J)
