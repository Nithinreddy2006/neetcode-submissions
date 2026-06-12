from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array (binary search on smaller = faster)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        lo, hi = 0, m

        while lo <= hi:
            # Partition both arrays
            i = (lo + hi) // 2          # partition index for nums1
            j = (m + n + 1) // 2 - i   # partition index for nums2

            # Left/right boundary values (handle edge cases with inf)
            left1  = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i]     if i < m else float('inf')
            left2  = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j]     if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                # Found the correct partition
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0

            elif left1 > right2:
                hi = i - 1   # move partition left in nums1
            else:
                lo = i + 1   # move partition right in nums1

        return 0.0  # unreachable for valid inputs