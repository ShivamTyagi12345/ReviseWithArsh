class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        peopleAware = [0]*n

        peopleAware[0] = 1

        total = 0
        MOD=  10**9 + 7

        for i in range(n):
            for j in range(delay , forget):
                if i+j < n:
                    peopleAware[i+j] = (peopleAware[i]+ peopleAware[i+j] ) %MOD
            total = (total + peopleAware[i]) % MOD
            if i >= forget:
                total = (total - peopleAware[i-forget] + MOD) %MOD
        return total
            

                
                    

        