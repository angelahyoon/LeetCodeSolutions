# Implement strStr()
def strStr(self, haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    elif needle not in haystack:
        return -1
    return 0