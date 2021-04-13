# Reverse Integer
def reverse(self, x: int) -> int:
        maxint = 2**31 - 1
        minint = 2**31
        y = 0
        
        if (x >= 0):
            while (x > 0):
                r = x % 10
                x = x // 10
                if (y > maxint // 10 or (y == maxint // 10 and r == 6)):
                    return 0
                y = y * 10 + r
            return y

        else:
            x *= -1
            while (x != 0):
                r = x % 10
                x = x // 10
                if (y > maxint // 10 or (y == maxint // 10 and r == 7)):
                    return 0
                y = y * 10 + r
            return y * -1