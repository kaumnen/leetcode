class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target > nums[-1]:
                return len(nums)
            elif target < nums[0]:
                return 0
            else:
                for i in nums:
                    if i > target:
                        return nums.index(i)
