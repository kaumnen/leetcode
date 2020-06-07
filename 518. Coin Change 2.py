class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        temp = [0 for x in range(amount+1)]
        temp[0] = 1
        for coin in coins:
            for i in range(len(temp)):
                if i >= coin:
                    temp[i] += temp[i - coin]
        return temp[-1]
