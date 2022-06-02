# https://leetcode.com/problems/transpose-matrix/solution/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        matrix1 = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(matrix[j][i])
            matrix1.append(temp)
        return(matrix1)
        