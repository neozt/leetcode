from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        n = len(senate)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(n)
            else:
                dire.append(n)

            n += 1

        return 'Radiant' if radiant else 'Dire'


print(Solution().predictPartyVictory('RD'))
print(Solution().predictPartyVictory('RDD'))
print(Solution().predictPartyVictory('DDRRR'))
print(Solution().predictPartyVictory('RRDDD'))
