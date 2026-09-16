class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        print(hashmap)
        result = []
        for j in range(k):
            largest = 0
            largest_key = ""
            for key in hashmap:
                print("Largest: ",largest)
                print("Key", key)
                if hashmap[key] > largest:
                    largest = hashmap[key]
                    largest_key = key

            result.append(largest_key)
            del hashmap[largest_key]
        return result
                
            