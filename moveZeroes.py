# Move Zeroes
def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = [0] * len(nums)
        n = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                a[n] = nums[i]
                n += 1
        nums[:] = a