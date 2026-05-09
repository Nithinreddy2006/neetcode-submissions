class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # Create a count array for 26 lowercase letters
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use tuple of counts as key
            key = tuple(count)
            anagram_groups[key].append(s)
        
        return list(anagram_groups.values())    