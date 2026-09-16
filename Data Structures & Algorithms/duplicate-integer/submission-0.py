class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        
        new = set(nums)
        if (len(new) != length):
            return True
        else:
            return False