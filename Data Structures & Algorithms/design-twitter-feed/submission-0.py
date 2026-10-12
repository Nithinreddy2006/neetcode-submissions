import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)    # userId -> list of (time, tweetId)
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Users whose tweets appear in the feed: self + followees
        users = self.following[userId] | {userId}

        # Max-heap (negate time) seeded with each user's most recent tweet
        heap = []
        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                t, tid = self.tweets[u][idx]
                heap.append((-t, tid, u, idx))
        heapq.heapify(heap)

        feed = []
        while heap and len(feed) < 10:
            _, tid, u, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx > 0:
                t, next_tid = self.tweets[u][idx - 1]
                heapq.heappush(heap, (-t, next_tid, u, idx - 1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)