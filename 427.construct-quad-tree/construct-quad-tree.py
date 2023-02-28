from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        total = sum([sum(row) for row in grid])
        if total == 0 or total == n * n:
            return Node(0 if total == 0 else 1, 1, None, None, None, None)
        mid = n >> 1
        topLeft = [row[:mid] for row in grid[:mid]]
        topRight = [row[mid:] for row in grid[:mid]]
        bottomLeft = [row[:mid] for row in grid[mid:]]
        bottomRight = [row[mid:] for row in grid[mid:]]
        return Node(1, 0, self.construct(topLeft), self.construct(topRight), self.construct(bottomLeft), self.construct(bottomRight))