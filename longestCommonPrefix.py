# Longest Common Prefix
def longestCommonPrefix(self, strs: List[str]) -> str:
        # consists of only lower-case English letters
        
        if (len(strs) == 0):
            return ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            while(strs[i].find(prefix) != 0):
                prefix = prefix[:-1]
            if (len(prefix) == 0):
                return ""
        
        return prefix