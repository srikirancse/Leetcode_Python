class Solution:
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        list(set(points)).sort()
        return points == sorted((points[0][0] + points[-1][0] - x, y) for x, y in points)
