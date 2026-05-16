class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        from collections import Counter

        need = Counter(t)      # characters we need
        have = {}              # characters we currently have in window
        formed = 0             # how many unique chars satisfy their required count
        required = len(need)

        left = 0
        best = ""

        for right, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1

            # Check if this character's count now satisfies the requirement
            if ch in need and have[ch] == need[ch]:
                formed += 1

            # Try to shrink the window from the left
            while formed == required:
                window = s[left:right + 1]
                if not best or len(window) < len(best):
                    best = window

                # Remove leftmost character
                left_ch = s[left]
                have[left_ch] -= 1
                if left_ch in need and have[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1

        return best