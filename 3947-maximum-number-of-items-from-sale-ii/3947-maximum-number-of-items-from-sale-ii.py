class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cnt = [0] * (n + 1)
        for f, _ in items:
            cnt[f] += 1
        mult = [0] * (n + 1)
        for f in range(1, n + 1):
            mult[f] = sum(cnt[f::f])

        min_price = min(p for _, p in items)
        keys = sorted((p << 17) | (mult[f] - 1) for f, p in items)

        rem, taken = budget, 0
        mask = (1 << 17) - 1
        for key in keys:
            price, gifts = key >> 17, key & mask
            if price >= 2 * min_price:
                break
            t = min(gifts, rem // price)
            taken += t
            rem -= t * price
            if t < gifts:
                break
        return 2 * taken + rem // min_price