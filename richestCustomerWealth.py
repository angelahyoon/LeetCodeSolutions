def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_list = []
        
        for i in range(len(accounts)):
            n = 0
            for j in range(len(accounts[i])):
                n += accounts[i][j]
            sum_list.append(n)
        
        return max(sum_list)