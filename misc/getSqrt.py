class Solution(object):

    @staticmethod
    def getSqrt(min, max, x):

        while (True):
            mid = int((max - min +1) / 2) + min
            mm = mid * mid
            #print (min, mid, max, mm, x)
            if mm == x:
                return mid
            elif mm < x:
                nextSqrt = (mid + 1) * (mid + 1)
                if nextSqrt == x:
                    return mid + 1
                elif nextSqrt > x:
                    return mid
                min = mid
            else:
                prevSprt = (mid - 1) * (mid - 1)
                if prevSprt <= x: return mid - 1
                max = mid

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return Solution.getSqrt(0, 2 ** 32, x)

    @staticmethod
    def checkSqrt(min, max, x):

        while (max >= min ):
            mid = int((max - min +1) / 2) + min
            mm = mid * mid
            print (min, mid, max, mm, x)

            if mm == x:
                return True
            elif mm < x:
                min = mid +1
            else:
                max = mid -1
        return False

    def isPerfectSquare(self, x):
        """
        :type x: int
        :rtype: int
        """
        return Solution.checkSqrt(0, 2 ** 32, x)

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPerfectSquare(25))
