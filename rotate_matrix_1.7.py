# Problem 1.7 CTCI
# Leetcode problem-> 48. Rotate Image
# Solution: First transpose(rows become columns, columns become rows) matrix
# then reverse the rows in the transposed matrix

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix)
                
        def transpose(matrix):
            for i in range(num_rows):
                for j in range(num_cols):
                    if j > i:
                        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                        
        def reverse_rows(matrix):
            for i in range(num_rows):
                matrix[i] = matrix[i][::-1]
                
        transpose(matrix)
        reverse_rows(matrix)
        
                    
        

