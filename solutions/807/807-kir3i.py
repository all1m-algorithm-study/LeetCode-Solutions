class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        skyline = []

        for v_line in grid:
            skyline.append([max(v_line)] * len(grid))

        for x, h_line in enumerate(list(zip(*grid))):
            max_h = max(h_line)
            for y in range(len(skyline)):
                skyline[y][x] = min(skyline[y][x], max_h)

        ans = sum([sum(l) for l in skyline]) - sum([sum(l) for l in grid])
        return ans