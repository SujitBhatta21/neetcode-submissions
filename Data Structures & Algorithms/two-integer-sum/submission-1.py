class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        hashmap = {}

        for i in range(N):
            toFind = target - nums[i] 
            if toFind in hashmap:
                return [hashmap[toFind], i]
            else:
                hashmap[nums[i]] = i
        return