class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        
        for i in range(rows):
            for j in range(i+1,rows):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        
        for row in range(rows):
            for i in range(cols//2):
                temp = matrix[row][i]
                matrix[row][i] = matrix[row][cols-1-i]
                matrix[row][cols-1-i] = temp
                
        return matrix
