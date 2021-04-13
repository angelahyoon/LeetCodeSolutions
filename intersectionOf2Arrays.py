# Intersection of Two Arrays II
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        shared_items = []
        
        for i in nums1:
            if i not in count1:
                count1[i] = 1
            else:
                count1[i] += 1
        
        for i in nums2:
            if i in count1 and count1[i] != 0:
                    shared_items.append(i)
                    count1[i] -= 1
        
        return shared_items