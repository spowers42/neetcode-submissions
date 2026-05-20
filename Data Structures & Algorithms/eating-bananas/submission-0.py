from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1  # eating 1 banana an hour
        max_k = max(piles)  # then it would take len(piles) hours
        best_k = max_k
        while min_k <= max_k:
            k = (min_k + max_k) // 2
            time_taken = self.eat_bananas(piles, k)
            if time_taken > h:
                min_k = k + 1
            else:
                best_k = k
                max_k = k - 1

        return best_k

    def eat_bananas(self, piles: List[int], k: int) -> int:
        # return the hours needed to eat the bananas
        return sum([ceil(p / k) for p in piles])
