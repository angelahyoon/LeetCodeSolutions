
# Two Sum
def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two nested lists add up the sum and put it into lists
        
    index_list = []
    length = len(nums)
    check = 0
    
    for i in range(length - 1):
        for j in range(i + 1, length):
            check = nums[i] + nums[j]
            if check == target:
                index_list.append(i)
                index_list.append(j)
                return index_list