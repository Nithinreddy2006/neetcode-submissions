from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        num_max = sum(1 for c in counts.values() if c == max_freq)
        
        # Formula: (max_freq - 1) full cycles of length (n + 1), 
        # plus num_max tasks for the last partial cycle
        intervals = (max_freq - 1) * (n + 1) + num_max
        
        # Can't be less than total number of tasks
        return max(intervals, len(tasks))