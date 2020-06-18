class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        length = len(citations)
        
        first = 0
        count = length
        
        while count > 0:
            step = count // 2
            mid = first + step
            if citations[mid] < length - mid:
                first = mid + 1
                count -= (step + 1)
            else:
                count = step
        
        return length - first
