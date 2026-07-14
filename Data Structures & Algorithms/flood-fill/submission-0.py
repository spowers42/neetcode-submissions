class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target_color = image[sr][sc]
        ROWS = len(image)
        COLUMNS = len(image[0])
        if target_color == color:
            # we aren't actually going to modify anything in this case
            return image

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLUMNS or image[r][c] != target_color:
                return

            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)
        return image
