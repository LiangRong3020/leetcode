class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        x_max = [0 for _ in range(n)]
        y_max = x_max[:]
        finnal_max = x_max[:]

        for i in range(n):
            x_max[i] = max(grid[i])

        for j in range(n):
            for i in range(n):
                y_max[j] = max(y_max[j], grid[i][j])

        increase_total = 0
        for i in range(n):
            for j in range(n):
                tmp_max = min(y_max[j], x_max[i])
                if grid[i][j] < tmp_max:
                    increase_total += (tmp_max - grid[i][j])

        return increase_total