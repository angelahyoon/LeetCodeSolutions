# Fizz Buzz
def fizzBuzz(self, n: int) -> List[str]:
        
        l = list(range(1, n+1))
        for i in range(n):
            if l[i] % 15 == 0:
                l[i] = "FizzBuzz"
            elif l[i] % 3 == 0:
                l[i] = "Fizz"
            elif l[i] % 5 == 0:
                l[i] = "Buzz"
            else:
                l[i] = str(l[i])
        return l