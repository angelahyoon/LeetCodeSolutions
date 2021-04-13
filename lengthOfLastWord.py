# Length of Last Word
def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if words == []:
            return 0
        return len(words[-1])
