# Contains Duplicate
def containsDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        d_nums = set(nums)
        l1 = len(d_nums)
        return l != l1