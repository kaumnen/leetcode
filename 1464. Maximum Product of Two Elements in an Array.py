class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp = max(nums)
        
        if nums.count(max(nums)) > 1:
            return (max(nums) - 1) ** 2
        
        else:
            for i in range(max(nums)):
                temp -= 1
                
                if temp in nums:
                    return (max(nums) - 1) * (temp - 1)
