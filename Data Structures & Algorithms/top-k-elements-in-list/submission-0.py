class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset = {}
        result = []

        for i in range(len(nums)):
            if nums[i] in hashset:
                hashset[nums[i]] += 1
            else:
                hashset[nums[i]] = 1

        while k != 0:
            largestKey = 0
            largestValue = 0

            for key in hashset:
                if hashset[key] > largestValue:
                    largestValue = hashset[key]
                    largestKey = key
            
            result.append(largestKey)

            # Remove current greatest from the hashset.
            hashset.pop(largestKey)
            # Reducing k by 1.
            k -= 1
            

        return result
