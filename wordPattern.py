# Word Pattern
def wordPattern(self, pattern: str, s: str) -> bool:
        letters = set(pattern)
        words = s.split()
        
        if len(letters) != len(set(words)) or len(pattern) != len(words):
            return False
        else:
            comp = zip(pattern, words)
            res = all((c1[0] == c2[0]) == (c1[1] == c2[1]) for c1 in comp for c2 in comp)
            return res