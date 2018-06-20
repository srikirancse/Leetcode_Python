class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        elements_count = rows * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    matrix[i][j] = elements_count

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    continue

                up = matrix[i - 1][j] if i > 0 else elements_count
                left = matrix[i][j - 1] if j > 0 else elements_count

                matrix[i][j] = min([up, left]) + 1

        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if matrix[i][j] == 0:
                    continue

                down = matrix[i + 1][j] if i < rows - 1 else elements_count
                right = matrix[i][j + 1] if j < cols - 1 else elements_count

                matrix[i][j] = min(min([down, right]) + 1, matrix[i][j])

        return matrix
