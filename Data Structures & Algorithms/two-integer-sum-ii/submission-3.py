class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while r != l:
            temp = numbers[l] + numbers[r]
            if temp == target:
                return [l+1, r+1]
            if temp > target:
                r -= 1
            else:
                l += 1
            
        


        