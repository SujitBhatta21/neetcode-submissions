class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Heap.
        freq = collections.Counter(nums)
        o_freq = [[v, k] for (k, v) in freq.items()]

        self.minHeap = o_freq
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
        ans = [item[1] for item in self.minHeap]
        return ans