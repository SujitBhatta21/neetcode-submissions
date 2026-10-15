class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        freq = [val for _, val in count.items()]

        self.maxHeap = freq
        heapq.heapify_max(self.maxHeap)
        queue = deque()
        time = 0

        while queue or self.maxHeap:
            # Tghings
            if queue and queue[0][1] == time:
                [a, b] = queue.popleft()
                heapq.heappush_max(self.maxHeap, a)

            if self.maxHeap:
                curr = heapq.heappop_max(self.maxHeap) - 1
                if curr > 0:
                    queue.append([curr, time+n+1])

            time += 1


        return time
            
