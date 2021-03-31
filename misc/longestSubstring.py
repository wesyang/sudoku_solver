class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = len(s)
        if count == 0:
            return 0;

        start = 0
        lookup = set(s[start])
        mover = start + 1
        longest = mover - start

        while True:
            if mover >= count:
                break;

            key = s[mover]
            if key in lookup:
                t = mover - start
                if t > longest:
                    longest = t

                start += 1
                lookup = set(s[start])
                mover = start + 1
            else:
                lookup.add(s[mover])
                mover += 1

        tt = mover - start
        return tt if tt > longest else longest


if __name__ == "__main__":
    s = Solution()
    # input = "abcabcbb"
    input = "bbbbb"
    input = "pwwkew"
    print(s.lengthOfLongestSubstring(input))
