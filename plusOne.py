# Plus One
def plusOne(self, digits: List[int]) -> List[int]:
        n = ""
        for i in range(len(digits)):
            n += str(digits[i])
        n = int(n) + 1
        return map(int, str(n))