class Solution(object):
    def searchLeft(self, cur, height, i):
        if i == 0:
            return 0;

        for j in range(i):
            if height[j] >= cur:
                return i - j;
        return 0

    def searchRight(self, cur, height, length, i):
        if i == length:
            return 0;

        # print (length, i)
        for j in range(length - i - 1):
            idx = length - j - 1;
            if height[idx] >= cur:
                return idx - i;

        return 0;

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        max = 0;

        for i in range(l):
            left = self.searchLeft(height[i], height, i)
            right = self.searchRight(height[i], height, l, i)

            # print(left, right)
            longer = left if left > right else right
            a = longer * height[i]
            if a > max:
                max = a;

        # print (z)
        return max


if __name__ == "__main__":
    s = Solution()
    # t = [4,3,2,1,4]
    # print(s.maxArea(t))

