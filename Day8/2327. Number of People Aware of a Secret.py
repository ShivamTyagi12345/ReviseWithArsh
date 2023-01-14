class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        peopleAware = [0] * n
        total = 0
        peopleAware[0] = 1
        MOD = 10**9+7
        for i in range(0, n):
            for j in range(delay, forget):
                if i+j < n:
                    peopleAware[i+j] =(peopleAware[i+j]+ peopleAware[i])%MOD
            total = (total + peopleAware[i]) % MOD
            if i >= forget:
                total = (total - peopleAware[i-forget] + MOD) % MOD
        return total