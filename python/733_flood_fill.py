from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        self.fill_surrounding(image, sr, sc, image[sr][sc], color)
        return image


    def fill_surrounding(self, image: List[List[int]], sr: int, sc: int, from_color: int, to_color: int):
        m = len(image)
        n = len(image[0])
        if not (0 <= sr < m) or not (0 <= sc < n):
            return

        color = image[sr][sc]
        if (color != from_color):
            return

        image[sr][sc] = to_color
        self.fill_surrounding(image, sr+1, sc, from_color, to_color)
        self.fill_surrounding(image, sr-1, sc, from_color, to_color)
        self.fill_surrounding(image, sr, sc+1, from_color, to_color)
        self.fill_surrounding(image, sr, sc-1, from_color, to_color)
