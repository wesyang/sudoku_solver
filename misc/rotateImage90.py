class Solution(object):
    @staticmethod
    def vEdge(y1, y2, x, matrix):
        w = abs(y2 - y1) + 1
        for i in range(w if w > 0 else -w):
            y = y1 + i if y2 > y1 else y1 - i
            p = matrix[y][x]
            print(f' {x}, {y}-> {p}')

    @staticmethod
    def hEdge(x1, x2, y, matrix):
        w = abs(x2 - x1) + 1
        for i in range(w if w > 0 else -w):
            x = x1 + i if x2 > x1 else x1 - i
            p = matrix[y][x]
            print(f' {x}, {y}-> {p}')

    def print(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        l = len(matrix)
        if l < 2: return matrix

        print(matrix)
        for i in range(int(l / 2)):
            x = y = i
            w = int(l / (i + 1))
            print(x, y, w)
            Solution.vEdge(y + w - 1, y, x, matrix)
            print("---")
            Solution.hEdge(x + w - 1, x, y + w - 1, matrix)
            print("---")
            Solution.vEdge(y, y + w - 1, x + w - 1, matrix)
            print("---")
            Solution.hEdge(x, x + w - 1, y, matrix)
            print("---")

    def replaceEdge(self, x, y, w, i, matrix):

        items = [[x + i, y], [x, y + w - 1 - i], [x + w - 1 - i, y + w - 1], [x + w - 1, y + i]]
        first = items[0]
        saved = matrix[first[1]][first[0]]
        print(items)
        print(f"-- saved {saved} --")
        for m in range(len(items) - 1):
            tx = items[m][0]
            ty = items[m][1]
            sx = items[m + 1][0]
            sy = items[m + 1][1]
            matrix[ty][tx] = matrix[sy][sx]

        last = items[-1]
        matrix[last[1]][last[0]] = saved

    def rotateEdge(self, x, y, w, matrix):
        for i in range(w - 1):
            self.replaceEdge(x, y, w, i, matrix)
        print(f'rotate edge: {matrix}')

    def rotate(self, matrix):
        l = len(matrix)
        if l < 2: return matrix

        print(matrix)
        for i in range(int(l / 2)):
            x = y = i
            w = l - (i * 2)
            print(f'condition {x}, {y}, {w}')
            self.rotateEdge(x, y, w, matrix)

    def longestSubsequence(self, nums):
        l = len(nums)
        if l < 2: return l

        first = 0
        longest = 1

        for i in range(1, l):
            if nums[i] <= nums[i - 1]:
                newLen = i - first
                if newLen > longest:
                    longest = newLen
                first = i

        if first < (l - 1):
            newLen = i - first + 1
            if newLen > longest:
                longest = newLen

        return longest


if __name__ == "__main__":
    s = Solution()
    # test = [1, 3, 5, 4, 7, 8, 9, 1]
    test = [1, 1, 3, 2]
    result = s.longestSubsequence(test)
    print(result)

    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    # matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

    # s.rotate(matrix)
    # print(f'final {matrix}')
