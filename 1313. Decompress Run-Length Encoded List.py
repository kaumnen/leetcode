class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        freq = 0
        val = 1
        
        for i in range(len(nums)//2):
            for i in range(nums[freq]):
                
                result.append(nums[val])
                
            freq += 2
            val += 2
            
        return result
