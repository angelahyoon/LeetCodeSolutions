def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_kid = max(candies)
        result = [0] * len(candies)
        
        for i in range(len(candies)):
            if (max_kid - candies[i]) > extraCandies:
                result[i] = False
            else:
                result[i] = True
        return result