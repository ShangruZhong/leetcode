"""
    554. Brick Wall

"""
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if not wall:
            return -1

        rows = len(wall)
        count = {}
        for i in xrange(rows):
            pos = 0
            for j in xrange(len(wall[i]) - 1):
                pos += wall[i][j]
                if pos in count:
                    count[pos] += 1
                else:
                    count[pos] = 1
        if not count:
            return rows
        return rows - (sorted(count.items(), lambda x, y: cmp(x[1], y[1]), reverse=True))[0][1]