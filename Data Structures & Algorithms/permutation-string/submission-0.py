class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        from collections import Counter
        
        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])
        
        if window == s1_count:
            return True
        
        for i in range(len(s1), len(s2)):
            # Add new character entering the window
            window[s2[i]] += 1
            
            # Remove character leaving the window
            left_char = s2[i - len(s1)]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            
            if window == s1_count:
                return True
        
        return False