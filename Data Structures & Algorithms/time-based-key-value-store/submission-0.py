from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        # key -> list of (timestamp, value), always appended in increasing ts order
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store[key]
        if not pairs:
            return ""

        # Binary search: find rightmost ts <= timestamp
        # bisect_right on a list of tuples compares by first element (timestamp)
        idx = bisect_right(pairs, (timestamp, chr(127)))  # chr(127) > any printable char
        
        if idx == 0:
            return ""  # all timestamps are greater than requested
        
        return pairs[idx - 1][1]