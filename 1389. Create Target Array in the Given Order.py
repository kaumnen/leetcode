class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        temp = 0
        for i in index:
            if i == 0:
                result = [nums[temp]] + result
            else:
                result = result[:i] + [nums[temp]] + result[i:] 
            temp += 1
        return result
