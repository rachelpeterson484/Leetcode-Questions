class Solution:
    grid = []

    # Remove all 1's connected to this point
    def delete_island(self, i0, j0) -> None:
        def inGrid(x, y):
            return x >= 0 and x < len(self.grid) and y >= 0 and y < len(self.grid[0])

        for (i_off, j_off) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i = i0 + i_off
            j = j0 + j_off

            if not inGrid(i, j) or self.grid[i][j] == "0":
                continue

            self.grid[i][j] = "0"
            self.delete_island(i, j)

    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        self.grid = grid

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == "0":
                    continue

                n_islands += 1
                self.grid[i][j] = "0"
                self.delete_island(i, j)

        return n_islands

