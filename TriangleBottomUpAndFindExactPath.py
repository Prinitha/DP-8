'''
TC: O(n^2) - for going through every element in the triangle
SC: O(1) for computing the minimum total but O(n) for the last row 
            to determine the path
''' 
from collections import deque
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS, COLS = len(triangle), len(triangle[0])
        path = deque()
        for i in range(ROWS-2,-1,-1):
            newpath = [False for _ in range(len(triangle[-1]))]
            for j in range(0, len(triangle[i])):
                if triangle[i+1][j] <= triangle[i+1][j+1]:
                    triangle[i][j] += triangle[i+1][j]
                    newpath[j] = True
                else:
                    triangle[i][j] += triangle[i+1][j+1]
            path.appendleft(newpath)
        print(path)
        return triangle[0][0]    
s = Solution()
print(s.minimumTotal([[1],[10,2],[5,6,7],[20,30,3,4],[5,50,60,80,60],[7,8,6,5,4,5]]))
print(s.minimumTotal([[-10]]))
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))