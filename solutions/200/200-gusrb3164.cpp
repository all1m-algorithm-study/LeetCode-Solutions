class Solution
{
public:
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {1, -1, 0, 0};

    int numIslands(vector<vector<char>> &grid)
    {
        int result = 0;

        for (int y = 0; y < grid.size(); y++)
        {
            for (int x = 0; x < grid[0].size(); x++)
            {
                if (findIsland(x, y, grid))
                {
                    result++;
                }
            }
        }
        return result;
    }
    bool findIsland(int x, int y, vector<vector<char>> &grid)
    {
        if (x < 0 || x >= grid[0].size() || y < 0 || y >= grid.size() || grid[y][x] != '1')
        {
            return false;
        }
        grid[y][x] = '0'; //이제 방문한 지역이므로 중복 안되게 0으로 바꿔줌
        for (int i = 0; i < 4; i++)
        {
            findIsland(x + dx[i], y + dy[i], grid);
        }
        return true;
    }
};