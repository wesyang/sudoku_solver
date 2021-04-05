class Solution(object):
    def isSub (self, haystack, needle, idx, ln):
        delta = 1
        while True:
            if delta >= ln :
                break
            if haystack[idx + delta] != needle[delta]:
                return False
            delta += 1

        return True

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0

        if haystack == '':
            return -1

        lh = len (haystack)
        ln = len (needle)

        idx = 0
        while True:
            if (idx + ln) > lh :
                break;
            if haystack[idx] == needle[0]:
                if self.isSub (haystack, needle, idx, ln):
                    return idx
            idx += 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    haystack = ""
    needle = ""
    print(solution.strStr(haystack, needle))
