class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        factors = [2,3,5]
        ugly = 1

        for _ in range(n):
            ugly = heapq.heappop(heap)
            for factor in factors:
                new_ugly = ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return ugly