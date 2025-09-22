class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[0])):
                if max < sum(accounts[i]):
                    max = sum(accounts[i])
        
        return max