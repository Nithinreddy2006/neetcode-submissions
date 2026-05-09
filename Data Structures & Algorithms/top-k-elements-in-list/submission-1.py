from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        # Create buckets: index = frequency, value = list of numbers with that frequency
        # Maximum frequency can be at most len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # Collect top k frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):  # Start from highest frequency
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result