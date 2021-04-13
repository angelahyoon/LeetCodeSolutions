# Roman to Integer
def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
        n = 0
        i = 0
        
        while (i < len(s)):
            if (i == len(s) - 1):
                n += values[s[i]]
                break
            elif (values[s[i+1]] <= values[s[i]]):
                n += values[s[i]]
                i += 1
            else:
                n += (values[s[i+1]] - values[s[i]])
                i += 2
        return n