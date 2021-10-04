class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        length = len(grid)
        width = len(grid[0])

        around_cell = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        total_side = 0

        for i in range(length):
            for j in range(width):
                if grid[i][j] == 0:
                    continue

                for a in around_cell:
                    tmp_i = i + a[0]
                    tmp_j = j + a[1]

                    if tmp_i < 0 or tmp_j < 0 or tmp_i >= length or tmp_j >= width:
                        total_side += 1
                    else:
                        if grid[tmp_i][tmp_j] == 0:
                            total_side += 1

        return total_side