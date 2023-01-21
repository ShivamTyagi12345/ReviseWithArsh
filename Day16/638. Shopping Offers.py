class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def shopping_offer( needs, lookup = None):
            lookup = {} if lookup is None else lookup
            if str(needs) in lookup:
                return lookup[str(needs)]
            l = len(needs)
            
            # unbounded knapsack needs a min/max value
            min_price = sum(price[i] * needs[i] for i in range(l))
            
            for offer in special:
                if all([offer[i] <= needs[i] for i in range(l)]):
                    new_needs = [needs[i]- offer[i] for i in range(l)]
                    min_price = min(min_price, offer[-1]+ shopping_offer(new_needs, lookup))
                    lookup[str(needs)] = min_price
            return min_price
        return shopping_offer(needs, None)
        