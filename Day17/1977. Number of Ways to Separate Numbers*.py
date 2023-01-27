class Solution:
    def numberOfCombinations(self, s):
        def ranks(l):
            index = {v: i for i, v in enumerate(sorted(set(l)))}
            return [index[v] for v in l]

        def suffixArray(s):
            line = ranks(s)
            n, k, ans, sa = len(s), 1, [line], [0]*len(s)
            while k < n - 1:
                line = ranks(list(zip_longest(line, islice(line, k, None), fillvalue=-1)))
                ans, k = ans + [line], k << 1
            for i, k in enumerate(ans[-1]): sa[k] = i
            return ans, sa

        @lru_cache(None)
        def compare(i, j, l, k):
            a = (c[k][i], c[k][(i+l-(1<<k))%n])
            b = (c[k][j], c[k][(j+l-(1<<k))%n])
            return 0 if a == b else 1 if a < b else -1

        c, _ = suffixArray([int(i) for i in s])

        n, M = len(s), 10**9 + 7
        dp = [[0]*(n+1) for _ in range(n+1)]
        mp = [[0]*(n+1) for _ in range(n+1)]

        for k in range(n+1):
            dp[0][k] = 1
            mp[0][k] = 1

        for i in range(1, n+1):
            for k in range(1, i + 1):
                if s[i-k] == "0": continue
                dp[i][k] = mp[i-k][k-1]
                if i >= 2*k and compare(i-2*k, i-k, k, floor(log2(k))) >= 0:
                    dp[i][k] += dp[i-k][k]

            for k in range(n + 1):
                mp[i][k] = mp[i][k-1] + dp[i][k]

        return mp[-1][-1]