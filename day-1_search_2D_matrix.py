"""
Problem: search_2D_matrix
Link: https://leetcode.com/problems/search-a-2d-matrix/
Difficulty: Medium

My Strategy (in my own words):
1. Simple binary search in a 2D matrix.
2. Treat the 2D matrix as a 1D array by calculating the row and column indices. 
Main logic: mid_row = mid // num_cols and mid_col = mid % num_cols.
3. Use binary search to find the target value by adjusting the mid index accordingly.
4. If the target is found, return True; otherwise, return False.

Time Complexity:
- Brute Force: O(m * n) - Checking each element in the matrix.
- Optimized: O(log(m * n)) - Treating the matrix as a single array

Space Complexity:
O(1) - No additional space used for the search.

---

Python Solution:
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search considering thr elements of matrix as if they are in an array
        rows = len(matrix)
        cols = len(matrix[0])

        L,R = 0, rows*cols-1

        while L<=R:
            mid = (L+R) //2 
            mid_row = mid // cols  #important logic to handle matrix access
            mid_col = mid % cols

            #binary search logic
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                L = mid+1
            else:
                R = mid-1
        return False
