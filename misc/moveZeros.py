class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums: return nums;

        l = len(nums)
        if l < 2: return nums

        mover = 0;
        freeSlot = 0;
        while True:
            if mover >= l: break

            if nums[mover] != 0:
                if mover != freeSlot:
                    nums[freeSlot] = nums[mover]
                freeSlot += 1
            mover += 1

        while True:
            if freeSlot >= l: break

            nums[freeSlot] = 0
            freeSlot += 1

        return nums

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return nums;

        l = len(nums)

        mover = 0;
        freeSlot = 0;
        while True:
            if mover >= l: break

            if nums[mover] != val:
                if mover != freeSlot:
                    nums[freeSlot] = nums[mover]
                freeSlot += 1
            mover += 1

        while True:
            if freeSlot >= l: break

            nums.pop (freeSlot)
            l -= 1

        return nums



if __name__ == "__main__":
    s = Solution()
    t = [0, 0, 1, 2, 0, 0, 1]
    #print(s.moveZeroes(t))

    t = [0,1,2,2,3,0,4,2]
    print (s.removeElement(t, 2))