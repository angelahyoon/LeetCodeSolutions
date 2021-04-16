# Running Sum of 1D Array
def runningSum(self, nums: List[int]) -> List[int]:
    n = []
    j = 0
    for i in range(0, len(nums)):
        j += nums[i]
        n.append(j)
    return n