class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        minarr = [i[0] for i in costs]
        differ = [j - i for i,j in costs]
        return sum(minarr) + sum(sorted(differ)[:len(costs)//2])
