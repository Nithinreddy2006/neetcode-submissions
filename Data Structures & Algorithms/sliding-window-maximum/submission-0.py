from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()  # stores indices, monotonically decreasing by value

        for i, num in enumerate(nums):
            # Remove indices outside the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove indices whose values are less than current (useless)
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(i)

            # Start adding results once the first window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result     