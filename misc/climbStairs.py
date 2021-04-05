class Solution(object):

    def climb (self, n, cur,  lookup):
        if n == cur:
            return 1
        if cur > n:
            return 0

        if lookup[cur] > 0:
            return lookup[cur]

        lookup[cur] = self.climb(n, cur+1, lookup) + self.climb (n, cur+2, lookup)
        return lookup[cur]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        lookup = [0] * n
        print (lookup)
        return self.climb (n, 0,  lookup)


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(38))