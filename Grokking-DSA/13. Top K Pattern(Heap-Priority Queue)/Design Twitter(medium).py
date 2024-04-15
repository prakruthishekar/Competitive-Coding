# Design a simplified version of Twitter where users can post tweets, 
# follow/unfollow another user, and is able to see the 10 most recent
# tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with
# ID tweetId by the user userId. Each call to this function will be
# made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent
# tweet IDs in the user's news feed. Each item in the news feed must 
# be posted by users who the user followed or by the user themself. 
# Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId 
# started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId
# started unfollowing the user with ID followeeId.
 

# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet",
#  "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 
# tweet id -> [5], since user 1 is no longer following user 2.


from ast import List
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)   # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)   # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1  # this is used by min heap to find the latest tweet

    def getNewsFeed(self, userId: int):
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                print(self.tweetMap[followeeId])
                index = len(self.tweetMap[followeeId])-1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index-1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId,followeeId, index -1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        

twitter = Twitter()
twitter.postTweet(1, 5)  # User 1 posts a new tweet (id = 5).
print(twitter.getNewsFeed(1));  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    # User 1 follows user 2.
twitter.follow(2, 1)
twitter.follow(2, 3)
twitter.postTweet(3, 0);
twitter.postTweet(3, 1);
twitter.postTweet(2, 6); # User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 7)
twitter.postTweet(3, 8);
twitter.getNewsFeed(1);  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  # User 1 unfollows user 2.
print(twitter.getNewsFeed(1));  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
print(twitter.getNewsFeed(2));  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
