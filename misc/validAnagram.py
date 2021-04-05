class Solution(object):

    @staticmethod
    def findItem (idx, c, t, l):
        for i in range (idx, l):
            if t[i] == c:
                if i > idx:
                    temp = t[idx]
                    t[idx] = t[i]
                    t[i] = temp

                return True;
        return False

    @staticmethod
    def checkAnagram(s, t):
        l = len(s)
        if l != len(t): return False

        if l == 0: return True

        #for i, c in enumerate(s):
        #    print (s, t)
        #    if not Solution.findItem (i, c, t, l): return False

        lookup = {}
        for c in s:
            if (c in lookup) :
                lookup[c] = lookup[c] + 1
            else:
                lookup[c] = 1

        print (lookup)

        for i in t:
            if i in lookup:
                if lookup[i] <= 0 : return False
                lookup[i] = lookup[i] -1
            else:
                return False

        return True

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lt = [c for c in t]
        return  'true' if Solution.checkAnagram (s, lt) else 'false'


if __name__ == "__main__":
    s = "cact"
    t = "catk"
    solution = Solution()
    print(solution.isAnagram(s, t))
