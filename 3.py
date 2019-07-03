from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check  = 0
        que = deque()
        for word in s:
            if word in que:
                if que[0] == word:
                    que.popleft()
                    que.append(word)
                else:
                    while que[0] is not word:
                        que.popleft()
                    que.popleft()
                    que.append(word)
            else:
                que.append(word)
                check = max(check, len(que))
        return check