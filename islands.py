def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        num_islands = 0
        seen = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        island_q = []

        island_q.append((0, 0))

        while len(island_q) != 0:

            print(island_q)
            current = island_q.pop(0)

            if grid[current[0]][current[1]] == "1":

                for direction in directions:
                    x = current[0] + direction[0]
                    y = current[1] + direction[1]
                    if 0 <= x < m and 0 <= y < n:
                        seen.add((x, y))
                        island_q.append((x, y))

                    elif grid[x][y] == "0":
                        continue

                num_islands += 1

            else:
                continue

        return num_islands

print(numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
                  ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
