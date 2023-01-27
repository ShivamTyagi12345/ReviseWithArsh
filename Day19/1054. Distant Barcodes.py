def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = collections.Counter(barcodes)
        index, n = 0, len(barcodes)
        ans = [0] * n
        for code, freq in cnt.most_common():
            for _ in range(freq):
                if index >= n:
                    index = 1
                ans[index] = code
                index += 2
        return ans