class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        piles.sort()
        alex = [piles[i] if (i + 1) % 2 == 0 else 0 for i in range(len(piles))]
        lee = [piles[i] if (i + 1) % 2 == 1 else 0 for i in range(len(piles))]

        if sum(alex) > sum(lee):
            return True
        else:
            return False