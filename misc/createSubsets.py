class Solution(object):
    def getSubset(self, nums, result):

        newResult = [[]] + [cc.copy() for cc in result]

        for cc in newResult:
            cc.append(nums[-1])

        return result+ newResult

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        result = []
        for c in range(len(nums)):
            result = self.getSubset(nums[0:c + 1], result)

        return [[]] + result


if __name__ == "__main__":
    s = Solution()
    t = [1, 2, 3, 4]
    print(s.subsets(t))
