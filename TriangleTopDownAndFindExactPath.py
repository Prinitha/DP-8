'''
TC: O(n^2) - for going through every element in the triangle
SC: O(1) for computing the minimum total but O(n^2) for the last row 
            to determine the path
''' 
from collections import deque
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #Top Down Approach with computing the path
        ROWS, COLS = len(triangle), len(triangle[0])
        path = [[(triangle[0][0],0)]]
        for i in range(1,ROWS):
            l = len(triangle[i])
            newpath = []
            for j in range(0,l):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                    newpath.append((triangle[i][j],j))
                elif j == l-1:
                    triangle[i][j] += triangle[i-1][j-1]
                    newpath.append((triangle[i][j],j-1))
                else:
                    if triangle[i-1][j-1] <= triangle[i-1][j]:
                        triangle[i][j] += triangle[i-1][j-1]
                        newpath.append((triangle[i][j],j-1))
                    else:
                        triangle[i][j] += triangle[i-1][j]         
                        newpath.append((triangle[i][j],j))  
            path.append(newpath) 
        print(path)       
        return min(triangle[-1])    
s = Solution()
print(s.minimumTotal([[1],[10,2],[5,6,7],[20,30,3,4],[5,50,60,80,60],[7,8,6,5,4,5]]))
print(s.minimumTotal([[-10]]))
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))