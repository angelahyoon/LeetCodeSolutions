# Valid Anagram
def isAnagram(self, s: str, t: str) -> bool:
        # assume only lowercase alphabet
        # can just check if they have same or different lengths first
        
        a = {}
        b = {}
        
        for i in set(s):
            a[i] = s.count(i)
        for i in set(t):
            b[i] = t.count(i)
            
        if (a == b):
            return True
        else:
            return False