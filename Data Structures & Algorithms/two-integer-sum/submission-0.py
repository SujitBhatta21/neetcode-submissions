class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for r in range(n):
            temp = target - nums[r]
            
            if temp in nums:
                for i in range(r+1, n):
                    if nums[i] == temp:
                        return [r, i]
