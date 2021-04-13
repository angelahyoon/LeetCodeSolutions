# First Unique Character in a String
def firstUniqChar(self, s: str) -> int:
        # assume the string contains only lowercase letters
        
        dict = {}
        for i in s:
            dict[i] = dict.get(i, 0) + 1
        
        for i in range(len(s)):
            if (dict[s[i]] == 1):
                return i
        
        return -1