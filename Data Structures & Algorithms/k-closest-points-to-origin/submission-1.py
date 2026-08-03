from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a max-heap of size k (negate distances to simulate max-heap with heapq)
        heap = []
        
        for x, y in points:
            dist = x * x + y * y
            # Push the negative distance so the largest distance is at the top
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[x, y] for _, x, y in heap]