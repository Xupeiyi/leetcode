from typing import List

import collections
import itertools
import heapq


class Twitter:

    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.following = collections.defaultdict(set)
        self.tweets = collections.defaultdict(collections.deque)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = heapq.merge(*(self.tweets[u] for u in self.following[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

