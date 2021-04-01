class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if not s or length < numRows or numRows < 2:
            return s

        result = []
        [result.append([]) for i in range(numRows)]

        print(result)

        idx = 0
        vdir: bool = True

        for c in s:
            result[idx].append(c)
            print(idx, c, result[idx], result)
            if idx == 0:
                vdir = True
            elif idx == (numRows - 1):
                vdir = False

            idx = idx + 1 if vdir else idx - 1
        print(f'final {result} ')

        flat = [c for row in result for c in row]

        print(f'flat: {flat}')
        return ''.join(flat)


if __name__ == "__main__":
    s = Solution()
    t = "Paxy"
    print(s.convert(t, 4))
