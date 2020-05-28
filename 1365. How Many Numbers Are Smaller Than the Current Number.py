class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        temp = 0
        for number in nums:
            for i in range(len(nums)):
                if nums[i] < number:
                    temp += 1
            result.append(temp)
            temp = 0
        return result
